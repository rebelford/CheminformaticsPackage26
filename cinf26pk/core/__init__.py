"""
Core utilities for the CINF 26 Cheminformatics course package.

This subpackage provides general-purpose helper functions that are
used across multiple modules and notebooks. These utilities are not
specific to PubChem or to any single instructional module.

Typical use
-----------
In most notebooks, import individual functions directly from
``cinf26pk.core``:

>>> from cinf26pk.core import make_fixed_filename
>>> from cinf26pk.core import save_csv

Contents
--------
File and naming utilities
- make_filename
- make_fixed_filename

File I/O helpers
- save_csv
- save_json
- save_text
- load_cid_dict

General utilities
- chunk_list
"""

# ------------------------------------------------------------
# Filename utilities
# ------------------------------------------------------------
from .filenames import (
    make_filename,
    make_fixed_filename,
)

# ------------------------------------------------------------
# I/O utilities
# ------------------------------------------------------------
from .io import (
    save_csv,
    save_json,
    save_text,
    load_cid_dict,
)

# ------------------------------------------------------------
# General utilities
# ------------------------------------------------------------
from .utils import (
    chunk_list,
)

# ------------------------------------------------------------
# Public API
# ------------------------------------------------------------
__all__ = [
    "make_filename",
    "make_fixed_filename",
    "save_csv",
    "save_json",
    "save_text",
    "load_cid_dict",
    "chunk_list",
]
