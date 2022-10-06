"""
    Effective Properties of a Laminate. 

    @author: Dmytro Kuksenko
    @date: Sept 22, 2022
"""

import numpy as np
from preprocess import get_material_props
from composite_analysis.material import Material


def abd_estimation():

    params = get_material_props(file_name="composite_analysis/layup.yaml")

    mat = Material(
        params["name"],
        params["mech_props"],
        params["thickness"],
        params["dt"],
        params["dm"],
    )

    stiff_matrix = reduced_stiff_matrix(mat.props)

    q = []
    for angle in params["layup"]:
        if angle != 0:
            q.append(matrix_transform(stiff_matrix, angle))
        else:
            q.append(stiff_matrix)

    abd = abd_matrix(q, params["thickness"])
    print(f"The abd matrix is {abd}")


def reduced_stiff_matrix(data):

    q = np.zeros(shape=(3, 3), dtype=np.float32)
    E1 = data[0]
    E2 = data[1]
    nu12 = data[2]
    G12 = data[3]

    q[0, 0] = E1 * E2 / (E1 - nu12 * E1)
    q[0, 1] = nu12 * E1 * E2 / (E1 - E2 * nu12**2)
    q[1, 1] = E1 * E2 / (E1 - E2 * nu12**2)
    q[2, 2] = G12

    return q


def matrix_transform(q, theta):

    t = np.zeros(shape=(3, 3), dtype=np.float32)

    m = np.cos(theta)
    n = np.sin(theta)

    t = np.array(
        [
            [m**2, n**2, 2 * m * n],
            [n**2, m**2, -2 * m * n],
            [-m * n, m * n, m**2 - n**2],
        ]
    )

    q_tr = np.dot(np.linalg.inv(t), q)

    return q_tr


def abd_matrix(q_sum, thx):

    a = np.zeros(shape=(3, 3), dtype=np.float32)
    b = np.zeros(shape=(3, 3), dtype=np.float32)
    d = np.zeros(shape=(3, 3), dtype=np.float32)

    for t, q in zip(q_sum, thx):
        a += q * t
        b += q * t**2
        d += q * t**3

    ab = np.vstack((a, (1 / 2) * b))
    bd = np.vstack((b, (1 / 3) * d))
    abd = np.hstack((ab, bd))

    return abd


def inverse_abd_matrix(abd):
    return np.linalg.inv(abd)


def effective_thermal_coef(alpha, theta=0):

    eff_alpha = np.zeros(shape=(2, 2), dtype=np.float32)

    m = np.cos(theta)
    n = np.sin(theta)

    eff_alpha[0, 0] = alpha[0, 0] * m**2 + alpha[1, 1] * n**2
    eff_alpha[1, 1] = alpha[0, 0] * n**2 + alpha[1, 1] * m**2
    eff_alpha[0, 1] = 2 * m * n * (alpha[0, 0] - alpha[1, 1])

    return eff_alpha


def effective_moisture_coef(beta, theta=0):

    eff_beta = np.zeros(shape=(2, 2), dtype=np.float32)

    m = np.cos(theta)
    n = np.sin(theta)

    eff_beta[0, 0] = beta[0, 0] * m**2 + beta[1, 1] * n**2
    eff_beta[1, 1] = beta[0, 0] * n**2 + beta[1, 1] * m**2
    eff_beta[0, 1] = 2 * m * n * (beta[0, 0] - beta[1, 1])

    return eff_beta


def thermal_resultants(q, alpha, thx, dt):

    f = np.zeros(shape=(6,), dtype=np.float32)

    for t in thx:
        f[0] += t * (
            q[0, 0] * alpha[0, 0] + q[0, 1] * alpha[1, 1] + q[0, 2] * alpha[0, 1]
        )
        f[1] += t * (
            q[1, 0] * alpha[0, 0] + q[1, 1] * alpha[1, 1] + q[1, 2] * alpha[0, 1]
        )
        f[2] += t * (
            q[2, 0] * alpha[0, 0] + q[2, 1] * alpha[1, 1] + q[2, 2] * alpha[0, 1]
        )

        f[3] += (3 * t**2) * (
            q[0, 0] * alpha[0, 0] + q[0, 1] * alpha[1, 1] + q[0, 2] * alpha[0, 1]
        )
        f[4] += (3 * t**2) * (
            q[1, 0] * alpha[0, 0] + q[1, 1] * alpha[1, 1] + q[1, 2] * alpha[0, 1]
        )
        f[5] += (3 * t**2) * (
            q[2, 0] * alpha[0, 0] + q[2, 1] * alpha[1, 1] + q[2, 2] * alpha[0, 1]
        )

    f[:3] = f[:3] * dt
    f[3:6] = f[3:6] * dt / 2

    return f


def moisture_resultants(q, beta, thx, dt):

    f = np.zeros(shape=(6,), dtype=np.float32)

    for t in thx:
        f[0] += t * (q[0, 0] * beta[0, 0] + q[0, 1] * beta[1, 1] + q[0, 2] * beta[0, 1])
        f[1] += t * (q[1, 0] * beta[0, 0] + q[1, 1] * beta[1, 1] + q[1, 2] * beta[0, 1])
        f[2] += t * (q[2, 0] * beta[0, 0] + q[2, 1] * beta[1, 1] + q[2, 2] * beta[0, 1])

        f[3] += (3 * t**2) * (
            q[0, 0] * beta[0, 0] + q[0, 1] * beta[1, 1] + q[0, 2] * beta[0, 1]
        )
        f[4] += (3 * t**2) * (
            q[1, 0] * beta[0, 0] + q[1, 1] * beta[1, 1] + q[1, 2] * beta[0, 1]
        )
        f[5] += (3 * t**2) * (
            q[2, 0] * beta[0, 0] + q[2, 1] * beta[1, 1] + q[2, 2] * beta[0, 1]
        )

    f[:3] = f[:3] * dt
    f[3:6] = f[3:6] * dt / 2

    return f


def get_average_strains(abd, res):
    strain = np.dot(abd, res)
    return strain


def ply_strain(str, thx):
    ply_str = str[:3] + thx * str[3:6]
    return ply_str


def ply_stress(q, ply_str, dt, dm, alpha, beta):
    strain = []
    strain[0] = ply_str[0] - alpha[0, 0] * dt - beta[0, 0] * dm
    strain[1] = ply_str[1] - alpha[1, 1] * dt - beta[1, 1] * dm
    strain[2] = ply_str[2] - alpha[0, 1] * dt - beta[0, 1] * dm
    ply_stress = np.dot(q, strain)
    return ply_stress
