__all__ = ["ctl", "obs", "dat", "end"]


# standard library
from importlib.resources import files
from tomli import loads


# dependencies
import numpy as np


def _get_dtype(name: str, /) -> np.dtype:
    with (files("sam45") / "dtypes.toml").open() as f:
        text = f.read()

    consts = loads(text)["consts"]
    dtype = loads(text.format(**consts))[name]
    return np.dtype([(item["name"], item["dtype"]) for item in dtype])


ctl = _get_dtype("ctl")
"""Data type of the SAM45/CTL information."""

obs = _get_dtype("obs")
"""Data type of the SAM45/OBS information."""

dat = _get_dtype("dat")
"""Data type of the SAM45/DAT information."""

end = _get_dtype("end")
"""Data type of the SAM45/END information."""
