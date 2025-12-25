__all__ = ["ctl", "obs", "dat", "end"]


# standard library
from importlib.resources import files
from tomli import loads
from typing import Any


# dependencies
from numpy import dtype


def _get_dtype(name: str, /) -> dtype[Any]:
    with (files("sam45") / "dtypes.toml").open() as file:
        source = file.read()

    consts = loads(source)["consts"]
    fields = loads(source.format(**consts))[name]
    return dtype([(f["name"], f["dtype"]) for f in fields]).newbyteorder("<")


ctl = _get_dtype("ctl")
"""Structured data type of the SAM45/CTL information."""

obs = _get_dtype("obs")
"""Structured data type of the SAM45/OBS information."""

dat = _get_dtype("dat")
"""Structured data type of the SAM45/DAT information."""

end = _get_dtype("end")
"""Structured data type of the SAM45/END information."""
