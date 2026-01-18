"""
cinf26pk.core.filenames

Filename-generation utilities used throughout the CINF26
Cheminformatics course.

This module provides small, focused helpers for creating
consistent and reproducible filenames for data artifacts.

Design principles:
- No I/O beyond directory creation
- No domain-specific (PubChem / RDKit) logic
- Deterministic or versioned naming as appropriate

Functions
---------
make_filename(prefix, ext, folder)
make_fixed_filename(stem, ext, add_date)

Import statement:
from cinf26pk.core import filenames

"""

# ============================================================
# Imports
# ============================================================

from pathlib import Path
from datetime import datetime


# ============================================================
# Filename Functions
# ============================================================

def make_filename(prefix: str, ext: str = "csv", folder: str = "downloads") -> str:
    """
    Create a unique versioned filename of the form:

        prefix_YYYYMMDD_vN.ext

    Intended for exploratory or intermediate data artifacts where
    multiple versions may be created in a single day.

    Parameters
    ----------
    prefix : str
        Filename prefix.
    ext : str, default="csv"
        File extension (without dot).
    folder : str, default="downloads"
        Output directory.

    Returns
    -------
    str
        Full path to the generated filename.
    """
    folder_path = Path(folder)
    folder_path.mkdir(parents=True, exist_ok=True)

    date_str = datetime.now().strftime("%Y%m%d")
    base = f"{prefix}_{date_str}"

    existing = [
        f for f in folder_path.iterdir()
        if f.name.startswith(base) and f.suffix == f".{ext}"
    ]

    version = len(existing) + 1
    filename = f"{base}_v{version}.{ext}"

    return str(folder_path / filename)


def make_fixed_filename(
    stem: str,
    ext: str = "csv",
    add_date: bool = True
) -> str:
    """
    Create a deterministic filename of the form:

        stem[_YYYYMMDD].ext

    Intended for canonical or authoritative data artifacts that
    should not be auto-versioned.

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
        Generated filename (no directory component).
    """
    if add_date:
        date_str = datetime.now().strftime("%Y%m%d")
        return f"{stem}_{date_str}.{ext}"
    else:
        return f"{stem}.{ext}"


# ============================================================
# Exported Names
# ============================================================

__all__ = [
    "make_filename",
    "make_fixed_filename",
]
