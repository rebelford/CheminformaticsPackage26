"""
cinf26pk.core.io

File input/output helper functions used throughout the CINF26
Cheminformatics course.

This module provides small, focused utilities for:
- Saving CSV, JSON, and text files to disk
- Loading JSON files with PubChem CIDs as integer keys

Design principles:
- No network access
- No domain-specific (PubChem / RDKit) logic
- Safe defaults for student use
- Clear, explicit behavior

Functions
---------
save_csv(text, prefix, folder)
save_json(obj, prefix, folder)
save_text(text, prefix, ext, folder)
load_cid_dict(path)
"""

# ============================================================
# Imports
# ============================================================

import json
from pathlib import Path
from typing import Dict, Any

from cinf26pk.core.filenames import make_filename


# ============================================================
# File Saving Functions
# ============================================================

def save_csv(text: str, prefix: str = "data", folder: str = "downloads") -> str:
    """
    Save CSV-formatted text to disk using a versioned filename.

    Parameters
    ----------
    text : str
        CSV-formatted text.
    prefix : str, default="data"
        Filename prefix.
    folder : str, default="downloads"
        Output directory.

    Returns
    -------
    str
        Path to the saved file.
    """
    path = Path(make_filename(prefix, ext="csv", folder=folder))
    path.write_text(text, encoding="utf-8")
    print(f"[Saved] CSV file written to: {path}")
    return str(path)


def save_json(obj: Any, prefix: str = "data", folder: str = "downloads") -> str:
    """
    Save a Python object as a JSON file using a versioned filename.

    Parameters
    ----------
    obj : Any
        JSON-serializable Python object.
    prefix : str, default="data"
        Filename prefix.
    folder : str, default="downloads"
        Output directory.

    Returns
    -------
    str
        Path to the saved file.
    """
    path = Path(make_filename(prefix, ext="json", folder=folder))
    with path.open("w", encoding="utf-8") as f:
        json.dump(obj, f, indent=2, ensure_ascii=False, sort_keys=True)
    print(f"[Saved] JSON file written to: {path}")
    return str(path)


def save_text(text: str, prefix: str = "output", ext: str = "txt",
              folder: str = "downloads") -> str:
    """
    Save plain text to disk using a versioned filename.

    Parameters
    ----------
    text : str
        Text content.
    prefix : str, default="output"
        Filename prefix.
    ext : str, default="txt"
        File extension.
    folder : str, default="downloads"
        Output directory.

    Returns
    -------
    str
        Path to the saved file.
    """
    path = Path(make_filename(prefix, ext=ext, folder=folder))
    path.write_text(text, encoding="utf-8")
    print(f"[Saved] Text written to: {path}")
    return str(path)


# ============================================================
# JSON Utilities
# ============================================================

def load_cid_dict(path: str) -> Dict[int, int]:
    """
    Load a JSON dictionary whose keys are PubChem CIDs and convert
    all keys to integers.

    Parameters
    ----------
    path : str
        Path to the JSON file.

    Returns
    -------
    dict[int, int]
        Dictionary with integer CID keys.
    """
    path = Path(path)

    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    if not isinstance(data, dict):
        raise ValueError(f"[Error] JSON file does not contain a dictionary: {path}")

    cleaned: Dict[int, int] = {}

    for cid, count in data.items():
        try:
            cid_int = int(cid)
            count_int = int(count)
        except ValueError:
            print(f"[Warning] Skipping invalid entry: {cid} → {count}")
            continue

        cleaned[cid_int] = count_int

    print(f"[Loaded] {len(cleaned)} CIDs from {path}")
    return cleaned


# ============================================================
# Exported Names
# ============================================================

__all__ = [
    "save_csv",
    "save_json",
    "save_text",
    "load_cid_dict",
]
