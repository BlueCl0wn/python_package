import numpy as np
import sympy as sp

r, a = sp.symbols("r, a", real=True)
def vec(a:float, r: float) -> sp.MutableDenseMatrix:
    return sp.Matrix([[a],
                      [r]])

def free_path(d: float, n:float = 1) -> sp.MutableDenseMatrix:
    return sp.Matrix([[1,   0],
                      [d/n, 1]])

def ideal_lens(f: float) -> sp.MutableDenseMatrix:
    return sp.Matrix([[1,   -1/f],
                      [0,   1]])
thin_lens = ideal_lens

def curved_surface(R: float, n1:float, n2: float) -> sp.MutableDenseMatrix:
    return sp.Matrix([[1,   -(n2 - n1)/R],
                      [0,   1]])

def thick_lens(R1:float, R2: float, n:float, d:float) -> sp.MutableDenseMatrix:
    EFL = ((n-1) * (sp.S(1)/R1-sp.S(1)/R2) + (n-1)**2*d/(n*R1*R2))**(-1)
    return sp.Matrix([[1 + (n-1)/n*d/R2,    -EFL**(-1)],
                      [d/n,                 1 - (n-1)/n*d/R1]])

__all__ = ["np", "sp", "r", "a", "vec", "free_path", "ideal_lens", "thin_lens", "curved_surface", "thick_lens"]

sp.init_printing()

