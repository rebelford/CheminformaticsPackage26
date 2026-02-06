"""
CINF 26 Cheminformatics course helper package.

This package provides reusable utilities, data-access helpers, and
module-specific infrastructure used throughout the CINF 26 course
materials and Jupyter Book.

Package structure
-----------------
cinf26pk is organized into clear subpackages:

- core
    General-purpose utilities shared across the course
    (filenames, I/O helpers, small utilities)

- pubchem
    High-level wrappers for interacting with the PubChem PUG-REST API
    (search, property retrieval, robust HTTP access)



Recommended usage
-----------------
Students should generally import from subpackages explicitly:

>>> from cinf26pk.pubchem import pubchem_fastsimilarity
>>> from cinf26pk.core import make_fixed_filename
>>> from cinf26pk.mod10 import DATA_DIR

Direct imports from the package root are intentionally minimal.

Design philosophy
-----------------
- Explicit is better than implicit
- Subpackages define meaning and context
- This structure mirrors real-world scientific Python libraries
"""

# ============================================================
# Public subpackages
# ============================================================

from . import core
from . import pubchem


# ============================================================
# Exported names
# ============================================================

__all__ = [
    "core",
    "pubchem",
]
Here is the .init file within core, which has 3 python files, filenames.py,io.py and utils.pymy_packages/cinf26pk/cinf26pk/core/__init__.py"""
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
