import numpy as np

__all__ = ["np"]

def init_sympy() -> None:
    import numpy as np
    import sympy as sp
    import matplotlib.pyplot as plt

    sp.init_session()

    print("Additionaly imported:")
    print(">>> import numpy as np \n>>> import sympy as sp\n>>> import matplotlib.pyplot as plt")
