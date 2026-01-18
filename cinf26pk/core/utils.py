"""
cinf26pk.core.utils

General-purpose utility functions used throughout the CINF26
Cheminformatics course.

This module is intentionally domain-agnostic: it contains small,
reusable helpers that are not specific to PubChem, RDKit, or any
single instructional module.

Functions
---------
chunk_list(lst, size)
"""

# ============================================================
# Imports
# ============================================================

from typing import Iterable, TypeVar, List

T = TypeVar("T")


# ============================================================
# Utility Functions
# ============================================================

def chunk_list(lst: Iterable[T], size: int) -> List[List[T]]:
    """
    Split an iterable into successive fixed-size chunks.

    Parameters
    ----------
    lst : iterable
        Iterable to split into chunks.
    size : int
        Number of elements per chunk.

    Returns
    -------
    list[list]
        List of chunked sublists.

    Examples
    --------
    >>> chunk_list([1, 2, 3, 4, 5], size=2)
    [[1, 2], [3, 4], [5]]
    """
    if size <= 0:
        raise ValueError("chunk size must be a positive integer")

    lst = list(lst)  # ensure slicing works
    return [lst[i:i + size] for i in range(0, len(lst), size)]


# ============================================================
# Exported Names
# ============================================================

__all__ = [
    "chunk_list",
]
