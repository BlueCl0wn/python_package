"""
ToDo
"""

import numpy as np
import uncertainties as unc
import scipy as cp
import pint as ps

__all__ = ["np", "unc", "cp"]


def api() -> None:
    """Print the module docstring and full help for this module."""

    print(__doc__)
    # help(sys.modules[__name__])


if __name__ == "__main__":
    # print docs when env is started with "ipython -i -m myutils.envs.science
    api()
