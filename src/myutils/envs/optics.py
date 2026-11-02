"""SymPy ray-optics toolbox (ABCD matrices, convention: out = M @ (a, r)).

Matrices:
    vec(a, r)             ray vector (a, r)^T
    free_path(d, n=1)     free-space propagation over distance d in medium n
    ideal_lens(f) = thin_lens(f)
    curved_surface(R, n1, n2)
    thick_lens(R1, R2, n, d)

Symbols: r, a, f

from sympy import *
"""

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
    EFL = ((n - 1) * (S(1) / R1 - S(1) / R2) + (n - 1) ** 2 * d / (n * R1 * R2)) ** (-1)
    return Matrix(
        [[1 + (n - 1) / n * d / R2, -(EFL ** (-1))], [d / n, 1 - (n - 1) / n * d / R1]]
    )


init_printing()


def api() -> None:
    """Print the module docstring and full help for this module."""

    print(__doc__)
    # help(sys.modules[__name__])


__all__ = [name for name in globals() if not name.startswith("_")]

if __name__ == "__main__":
    # print docs when env is started with "ipython -i -m myutils.envs.optics
    api()
