__all__ = ["ctl", "obs", "dat", "end"]


# standard library
from mmap import mmap
from os import PathLike
from typing import Any


# dependencies
from numpy import frombuffer
from numpy.typing import NDArray
from . import dtypes


def ctl(log: PathLike[str] | str, /, *, validate: bool = True) -> NDArray[Any]:
    """Read a SAM45 log to extract the SAM45/CTL information.

    Args:
        log: Path to the SAM45 log.
        validate: Whether to validate the content of the read information.

    Returns:
        NumPy structured array containing the SAM45/CTL information.

    Raises:
        ValueError: Raised if the read information is invalid,
            i.e., the ``crec_type`` field of it is not ``b"L0"``.

    """
    start = None
    stop = dtypes.ctl.itemsize

    with open(log, "r+b") as f:
        mm = mmap(f.fileno(), 0)
        data = frombuffer(mm[start:stop], dtype=dtypes.ctl)

    if not validate or (data["crec_type"] == b"L0").all():
        return data
    else:
        raise ValueError("Invalid SAM45/CTL information (maybe truncated).")


def obs(log: PathLike[str] | str, /, *, validate: bool = True) -> NDArray[Any]:
    """Read a SAM45 log to extract the SAM45/OBS information.

    Args:
        log: Path to the SAM45 log.
        validate: Whether to validate the content of the read information.

    Returns:
        NumPy structured array containing the SAM45/OBS information.

    Raises:
        ValueError: Raised if the read information is invalid,
            i.e., the ``crec_type`` field of it is not ``b"L1"``.

    """
    start = dtypes.ctl.itemsize
    stop = dtypes.ctl.itemsize + dtypes.obs.itemsize

    with open(log, "r+b") as f:
        mm = mmap(f.fileno(), 0)
        data = frombuffer(mm[start:stop], dtype=dtypes.obs)

    if not validate or (data["crec_type"] == b"L1").all():
        return data
    else:
        raise ValueError("Invalid SAM45/OBS information (maybe truncated).")


def dat(log: PathLike[str] | str, /, *, validate: bool = True) -> NDArray[Any]:
    """Read a SAM45 log to extract the SAM45/DAT information.

    Args:
        log: Path to the SAM45 log.
        validate: Whether to validate the content of the read information.

    Returns:
        NumPy structured array containing the SAM45/DAT information.

    Raises:
        ValueError: Raised if the read information is invalid,
            i.e., the ``crec_type`` field of it is not ``b"L2"``.

    """
    start = dtypes.ctl.itemsize + dtypes.obs.itemsize
    stop = -dtypes.end.itemsize

    with open(log, "r+b") as f:
        mm = mmap(f.fileno(), 0)
        data = frombuffer(mm[start:stop], dtype=dtypes.dat)

    if not validate or (data["crec_type"] == b"L2").all():
        return data
    else:
        raise ValueError("Invalid SAM45/DAT information (maybe truncated).")


def end(log: PathLike[str] | str, /, *, validate: bool = True) -> NDArray[Any]:
    """Read a SAM45 log to extract the SAM45/END information.

    Args:
        log: Path to the SAM45 log.
        validate: Whether to validate the content of the read information.

    Returns:
        NumPy structured array containing the SAM45/END information.

    Raises:
        ValueError: Raised if the read information is invalid,
            i.e., the ``crec_type`` field of it is not ``b"ED"``.

    """
    start = -dtypes.end.itemsize
    stop = None

    with open(log, "r+b") as f:
        mm = mmap(f.fileno(), 0)
        data = frombuffer(mm[start:stop], dtype=dtypes.end)

    if not validate or (data["crec_type"] == b"ED").all():
        return data
    else:
        raise ValueError("Invalid SAM45/END information (maybe truncated).")
