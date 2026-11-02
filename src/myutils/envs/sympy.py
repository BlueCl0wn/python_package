"""Simple SymPy toolbox.

Ran commands:
    from sympy import *
    x, y, z, t = symbols("x y z t")
    k, m, n = symbols("k m n", integer=True)
    f, g, h = symbols("f g h", cls=Function)
    init_printing()

    from sympy import *
"""

from sympy import *

x, y, z, t = symbols("x y z t")
k, m, n = symbols("k m n", integer=True)
f, g, h = symbols("f g h", cls=Function)
init_printing()

__all__ = [name for name in globals() if not name.startswith("_")]


def api() -> None:
    """Print the module docstring and full help for this module."""

    print(__doc__)
    # help(sys.modules[__name__])


if __name__ == "__main__":
    # print docs when env is started with "ipython -i -m myutils.envs.sympy
    api()
