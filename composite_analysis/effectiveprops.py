"""
    Effective Properties of a Laminate. 

    @author: Dmytro Kuksenko
    @date: Sept 22, 2022
"""

import numpy as np


def estimation():
    # Mat Properties of the uni lamina (T300/5208)

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

    angles = [0, 90, 90, 0]
    thx = [0.2, 0.2, 0.2, 0.2]

    stiff_matrix = reduced_stiff_matrix(e1, e2, nu12, g12)

    q = []
    for angle in angles:
        if angle != 0:
            q.append(matrix_transform(stiff_matrix, angle))
        else:
            q.append(stiff_matrix)


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

    q_tr = np.dot(np.inv(t), q)

    return q_tr


def abd_assemble(q_sum, thx):

    a = np.zeros(shape=(3, 3), dtype=np.float32)
    b = np.zeros(shape=(3, 3), dtype=np.float32)
    d = np.zeros(shape=(3, 3), dtype=np.float32)

    for t, q in zip(q_sum, thx):
        a += q * t
        b += q * t**2
        d += q * t**3

    abd = np.hstack(np.vstack(a, (1 / 2) * b), np.vstack(b, (1 / 3) * d))

    return abd
