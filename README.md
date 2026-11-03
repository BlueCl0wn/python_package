# myutils

A personal collection of reusable Python utilities, scientific tools, and convenient interactive environments.

`myutils` provides a collection of functions and preconfigured environments for scientific computing, symbolic mathematics, and optics. It is primarily intended to simplify everyday calculations and workflows, particularly when working interactively with Python and IPython.

## Features

- **Symbolic mathematics:** Convenient SymPy imports and predefined symbols.
- **Geometrical optics:** ABCD ray-transfer matrices for optical systems, including thin and thick lenses.
- **Scientific computing:** Convenient access to NumPy, SciPy, and uncertainties.
- **Interactive environments:** Preconfigured namespaces designed for use in IPython and PTIPython.

## Installation

### Requirements

- Python ≥ 3.12

### Install from GitHub

Using `uv`:

```bash
uv add git+https://github.com/bluecl0wn/python_package
```

Alternatively, using `pip`:

```bash
pip install git+https://github.com/bluecl0wn/python_package
```

### Install for development

Clone the repository and install it in editable mode:

```bash
git clone https://github.com/bluecl0wn/python_package.git
cd python_package
uv sync --group dev
```

Editable installation is useful when developing the package, as changes to the source code are picked up without reinstalling it.

## Usage

### Basic usage
Supplies envs with pre-defined methods and variables mainly for live python sessions.

```cmd
ipython -i -m myutils.envs.sympy
```

or in ipython (or similar):
```python
from myutils.envs.sympy import *
```

### SymPy environment

The SymPy environment provides convenient access to the SymPy namespace without having to prefix every function with `sp.`.

```python


# Predefined symbols:
# x, y, z, t
# k, m, n (integers)
# f, g, h (functions)

expr = sin(x)**2 + cos(x)**2
simplify(expr)
# 1
```

The environment also enables SymPy's pretty-printing through `init_printing()`.

### Optics environment

The optics environment provides symbolic ray-transfer matrices (ABCD matrices) for geometrical optics.

```python
from myutils.envs.optics import *

# Define an optical system
M = free_path(10) @ ideal_lens(5)

# Define an input ray
ray = vec(0.1, 2)

# Calculate the output ray
ray_out = M @ ray
```

The ray vector convention is

\[
\mathbf{r} =
\begin{pmatrix}
\alpha \\
r
\end{pmatrix}
\]

where \(\alpha\) is the paraxial ray angle and \(r\) is the ray height.

Available functions:

| Function | Description |
|---|---|
| `vec(a, r)` | Construct a ray vector |
| `free_path(d, n=1)` | Propagation through a homogeneous medium |
| `ideal_lens(f)` | Ideal thin lens |
| `thin_lens(f)` | Alias for `ideal_lens(f)` |
| `curved_surface(R, n1, n2)` | Refraction at a spherical interface |
| `thick_lens(R1, R2, n, d)` | Thick-lens transfer matrix |

The matrices follow the convention

\[
\mathbf{r}_{\mathrm{out}} = M \mathbf{r}_{\mathrm{in}}.
\]

### Scientific computing environment

The science environment provides convenient imports for common scientific Python libraries.

```python
from myutils.envs.science import *

# Available modules:
np   # NumPy
cp   # SciPy
unc  # uncertainties
```

This is particularly useful in interactive sessions where these libraries are frequently needed.

## Development

The project uses [uv](https://docs.astral.sh/uv/) for dependency management and [Ruff](https://docs.astral.sh/ruff/) for linting and formatting.

Install development dependencies:

```bash
uv sync --group dev
```

Run the linter:

```bash
uv run ruff check .
```

Automatically fix supported linting issues:

```bash
uv run ruff check --fix .
```

Format the code:

```bash
uv run ruff format .
```

Run the test suite:

```bash
uv run pytest
```

Build the package:

```bash
uv build
```

## Dependencies

The package currently depends on:

- [NumPy](https://numpy.org/) – numerical computing
- [SciPy](https://scipy.org/) – scientific computing
- [SymPy](https://www.sympy.org/) – symbolic mathematics
- [uncertainties](https://pythonhosted.org/uncertainties/) – calculations with uncertainty propagation

## License

See [LICENSE](LICENSE) for licensing information.