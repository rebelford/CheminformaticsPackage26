"""
This subpackage provides high-level, student-safe wrappers around the
PubChem PUG-REST API. These functions are designed for instructional use,
robustness, and readability rather than maximum performance.

Typical use
-----------
In most notebooks, import PubChem tools from this subpackage directly:

>>> from cinf26pk.pubchem import pubchem_fastsimilarity
>>> from cinf26pk.pubchem import pubchem_properties_for_cids

Available functionality
------------------------
Search operations
- pubchem_fastsimilarity
- pubchem_fastidentity

Property retrieval
- pubchem_properties_for_cids

Low-level HTTP utilities
------------------------
Advanced users may also access the underlying HTTP helpers:

>>> from cinf26pk.pubchem import pubchem_get, pubchem_post

Design notes
------------
- All network operations include retry logic and basic error handling.
- Chunking and rate-limiting are handled internally where appropriate.
- Progress bars (tqdm) are used to provide feedback during long operations.
"""

# ============================================================
# High-level search functions
# ============================================================

from .search import (
    pubchem_fastsimilarity,
    pubchem_fastidentity,
)

# ============================================================
# Property retrieval
# ============================================================

from .properties import (
    pubchem_properties_for_cids,
)

# ============================================================
# Low-level HTTP helpers (advanced use)
# ============================================================

from .http import (
    pubchem_get,
    pubchem_post,
)

# ============================================================
# Exported names
# ============================================================

__all__ = [
    # Search
    "pubchem_fastsimilarity",
    "pubchem_fastidentity",

    # Properties
    "pubchem_properties_for_cids",

    # HTTP (advanced)
    "pubchem_get",
    "pubchem_post",
]

