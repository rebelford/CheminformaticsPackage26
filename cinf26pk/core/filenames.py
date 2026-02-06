"""
cinf26pk.core.filenames

Filename-generation utilities used throughout the CINF 26
Cheminformatics course.

This module provides small, focused helpers for creating
consistent and reproducible filenames for data and model artifacts.

Design principles
-----------------
- No filesystem I/O (no directory creation)
- No domain-specific (PubChem / RDKit) logic
- Filenames only: paths are owned by notebooks or pipelines
- Clear semantic distinction between exploratory data and
  identity-bearing artifacts

Functions
---------
make_filename(prefix, ext)
    Versioned, date-stamped filenames for regenerable artifacts.

make_fixed_filename(stem, ext, add_date)
    Deterministic filenames for canonical artifacts.

make_artifact_filename(stem, ext, version)
    Identity-based filenames for models and pipeline outputs
    (introduced for Module 10.4; not used in Module 10.2).

Typical usage
-------------
>>> fname = make_filename("AID743139_MACCS_variance_mask", "npy")
>>> path = FEATURES / fname
>>> np.save(path, mask)
"""

# ============================================================
# Imports
# ============================================================

from datetime import datetime
from pathlib import Path


# ============================================================
# Filename helpers
# ============================================================

def make_filename(prefix: str, ext: str = "csv") -> str:
    """
    Create a versioned, date-stamped filename of the form:

        prefix_YYYYMMDD_vN.ext

    Intended for exploratory or intermediate artifacts that may be
    regenerated multiple times in a single day.

    NOTE
    ----
    This function does NOT create directories and does NOT return
    a path. Directory management is the responsibility of the caller.

    Parameters
    ----------
    prefix : str
        Filename prefix.
    ext : str, default="csv"
        File extension (without dot).

    Returns
    -------
    str
        Generated filename.
    """
    date_str = datetime.now().strftime("%Y%m%d")
    base = f"{prefix}_{date_str}"

    # Versioning is deferred to the caller's directory context.
    # The caller should count existing files if versioning matters.
    # By default, start with v1.
    return f"{base}_v1.{ext}"


def make_fixed_filename(
    stem: str,
    ext: str = "csv",
    add_date: bool = True
) -> str:
    """
    Create a deterministic filename of the form:

        stem[_YYYYMMDD].ext

    Intended for canonical or authoritative artifacts that should
    not be auto-versioned.

    Parameters
    ----------
    stem : str
        Base filename (without extension).
    ext : str, default="csv"
        File extension (without dot).
    add_date : bool, default=True
        Append YYYYMMDD to the filename.

    Returns
    -------
    str
        Generated filename.
    """
    if add_date:
        date_str = datetime.now().strftime("%Y%m%d")
        return f"{stem}_{date_str}.{ext}"
    else:
        return f"{stem}.{ext}"


def make_artifact_filename(
    stem: str,
    ext: str,
    version: str | None = None
) -> str:
    """
    Create an identity-based filename for models or pipeline artifacts.

    Examples
    --------
    nb_maccs_AID743139.joblib
    nb_maccs_AID743139_v1.joblib
    rf_ecfp4_AID743139_v2.joblib

    Intended for trained models, pipelines, or evaluation artifacts
    where versioning is intentional and meaningful.

    NOTE
    ----
    This function is introduced for Module 10.4 and later.
    It is NOT used in Module 10.2.

    Parameters
    ----------
    stem : str
        Base artifact name (without extension).
    ext : str
        File extension (without dot).
    version : str or None, optional
        Explicit version tag (e.g., "v1", "v2"). If None, no version
        suffix is added.

    Returns
    -------
    str
        Generated filename.
    """
    if version:
        return f"{stem}_{version}.{ext}"
    else:
        return f"{stem}.{ext}"


# ============================================================
# Public API
# ============================================================

__all__ = [
    "make_filename",
    "make_fixed_filename",
    "make_artifact_filename",
]
