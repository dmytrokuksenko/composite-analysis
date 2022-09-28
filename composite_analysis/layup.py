"""
    Effective Properties of a Laminate. 

    @author: Dmytro Kuksenko
    @date: Sept 22, 2022
"""

import numpy as np


def estimation():

    # Material Properties of a unidirectional lamina (T300/5208)

    e1 = 136e03  # MPa
    e2 = 9.80e03  # MPa
    e3 = 9.80e03  # MPa
    g12 = 4.7e03  # MPa
    g13 = 4.7e03  # MPa
    g23 = 4.7e03  # MPa
    nu12 = 0.28
    nu13 = 0.28
    nu23 = 0.15
    rho = 1.54e-09  # ton/mm^3
    f1t = 1550  # MPa
    f1c = 1090  # MPa
    f2t = 59  # MPa
    f3t = 59  # MPa
    f4 = 128  # MPa
    f6 = 75  # MPa

    thermal_coeff = [1, 1, 1]
    moisture_coeff = [1, 1, 1]

    angles = (0, 90, 90, 0)
    thx = (0.2, 0.2, 0.2, 0.2)
    resultants = [1, 0, 0, 0, 0, 0]

    stiff_matrix = reduced_stiff_matrix(e1, e2, nu12, g12)

    q = []
    for angle in angles:
        if angle != 0:
            q.append(matrix_transform(stiff_matrix, angle))
        else:
            q.append(stiff_matrix)

    abd = abd_matrix(q, thx)
    print(f"The abd matrix is {abd}")


def reduced_stiff_matrix(e1, e2, nu12, g12):

    q = np.zeros(shape=(3, 3), dtype=np.float32)

    q[0, 0] = e1 * 22 / (e1 - nu12 * e2)
    q[0, 1] = nu12 * e1 * e2 / (e1 - e2 * nu12**2)
    q[1, 1] = e1 * e2 / (e1 - e2 * nu12**2)
    q[2, 2] = g12

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
