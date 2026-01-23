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
