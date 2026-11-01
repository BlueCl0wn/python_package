import numpy as np
from sympy import *

r, a, f = symbols("r, a, f", real=True)


def vec(a: float, r: float) -> MutableDenseMatrix:
    return Matrix([[a], [r]])


def free_path(d: float, n: float = 1) -> MutableDenseMatrix:
    return Matrix([[1, 0], [d / n, 1]])


def ideal_lens(f: float) -> MutableDenseMatrix:
    return Matrix([[1, -1 / f], [0, 1]])


thin_lens = ideal_lens


def curved_surface(R: float, n1: float, n2: float) -> MutableDenseMatrix:
    return Matrix([[1, -(n2 - n1) / R], [0, 1]])


def thick_lens(R1: float, R2: float, n: float, d: float) -> MutableDenseMatrix:
    EFL = (
        (n - 1) * (S(1) / R1 - S(1) / R2) + (n - 1) ** 2 * d / (n * R1 * R2)
    ) ** (-1)
    return Matrix(
        [[1 + (n - 1) / n * d / R2, -(EFL ** (-1))], [d / n, 1 - (n - 1) / n * d / R1]]
    )


__all__ = [
    name for name in globals()
    if not name.startswith("_")
]

init_printing()
