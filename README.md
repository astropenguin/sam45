# SAM45

[![Release](https://img.shields.io/pypi/v/sam45?label=Release&color=cornflowerblue&style=flat-square)](https://pypi.org/project/sam45/)
[![Python](https://img.shields.io/pypi/pyversions/sam45?label=Python&color=cornflowerblue&style=flat-square)](https://pypi.org/project/sam45/)
[![Downloads](https://img.shields.io/pypi/dm/sam45?label=Downloads&color=cornflowerblue&style=flat-square)](https://pepy.tech/project/sam45)
[![DOI](https://img.shields.io/badge/DOI-10.5281/zenodo.18055352-cornflowerblue?style=flat-square)](https://doi.org/10.5281/zenodo.18055352)
[![Tests](https://img.shields.io/github/actions/workflow/status/astropenguin/sam45/tests.yaml?label=Tests&style=flat-square)](https://github.com/astropenguin/sam45/actions)

NRO/SAM45 log data reader

## Installation

```shell
pip install sam45
```

## Usage

The following functions will read a SAM45 log to extract each information as [a NumPy structured array](https://numpy.org/doc/stable/user/basics.rec.html).

```python
import sam45

data_ctl = sam45.read.ctl("/path/to/log")
data_obs = sam45.read.obs("/path/to/log")
data_dat = sam45.read.dat("/path/to/log")
data_end = sam45.read.end("/path/to/log")
```

## Data types

The data type of each information is defined as [a NumPy structured data type](https://numpy.org/doc/stable/reference/arrays.dtypes.html).
It complies with the definition as of December 5, 2025.

```python
import sam45

dtype_ctl = sam45.dtypes.ctl
dtype_obs = sam45.dtypes.obs
dtype_dat = sam45.dtypes.dat
dtype_end = sam45.dtypes.end
```
