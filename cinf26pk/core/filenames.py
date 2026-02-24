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
"""
cinf26pk.core.filenames

Filename-generation utilities for CINF 26.
"""

from datetime import datetime
from pathlib import Path


# ============================================================
# Versioned exploratory artifacts
# ============================================================

def make_filename(
    prefix: str,
    ext: str,
    directory: Path
) -> str:
    """
    Create a versioned, date-stamped filename:

        prefix_YYYYMMDD_vN.ext

    Version auto-increments based on existing files in directory.
    """

    if not isinstance(directory, Path):
        raise TypeError("directory must be a pathlib.Path object")

    date_str = datetime.now().strftime("%Y%m%d")
    base = f"{prefix}_{date_str}"

    existing_versions = []

    if directory.exists():
        for f in directory.iterdir():
            if f.is_file() and f.suffix == f".{ext}":
                name = f.stem
                if name.startswith(base):
                    parts = name.split("_v")
                    if len(parts) == 2 and parts[0] == base:
                        try:
                            version = int(parts[1])
                            existing_versions.append(version)
                        except ValueError:
                            pass

    next_version = max(existing_versions, default=0) + 1

    return f"{base}_v{next_version}.{ext}"


# ============================================================
# Deterministic canonical artifacts
# ============================================================

def make_fixed_filename(
    stem: str,
    ext: str = "csv",
    add_date: bool = True
) -> str:
    """
    Create deterministic filename:

        stem[_YYYYMMDD].ext
    """

    if add_date:
        date_str = datetime.now().strftime("%Y%m%d")
        return f"{stem}_{date_str}.{ext}"
    else:
        return f"{stem}.{ext}"


# ============================================================
# Identity-based model artifacts
# ============================================================

def make_artifact_filename(
    stem: str,
    ext: str,
    version: str | None = None
) -> str:
    """
    Create identity-based artifact filename:

        stem[_version].ext
    """

    if version:
        return f"{stem}_{version}.{ext}"
    else:
        return f"{stem}.{ext}"


__all__ = [
    "make_filename",
    "make_fixed_filename",
    "make_artifact_filename",
]