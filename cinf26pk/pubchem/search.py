"""
PubChem similarity and identity search utilities.

This module provides high-level wrappers for PubChem fast similarity
and identity searches using the PUG-REST API.

Functions
---------
- pubchem_fastsimilarity : 2D similarity search using SMILES
- pubchem_fastidentity   : Identity-based search using SMILES
"""

# ============================================================
# Imports
# ============================================================

from typing import List
from urllib.parse import quote

from .http import pubchem_get, pubchem_post

# ============================================================
# Constants
# ============================================================

PUG_BASE = "https://pubchem.ncbi.nlm.nih.gov/rest/pug"

# ============================================================
# PubChem Search Functions
# ============================================================

def pubchem_fastsimilarity(smiles: str, threshold: int = 90) -> List[int]:
    """
    Perform a PubChem 2D fast similarity search for a SMILES string.

    Parameters
    ----------
    smiles : str
        SMILES string to search.
    threshold : int, default=90
        Tanimoto similarity threshold (0–100).

    Returns
    -------
    list[int]
        List of matching PubChem CIDs. Empty if the query fails.
    """
    if not isinstance(smiles, str) or not smiles.strip():
        print("[Error] Invalid SMILES input.")
        return []

    smi_enc = quote(smiles)

    url = (
        f"{PUG_BASE}/compound/fastsimilarity_2d/"
        f"smiles/cids/txt?smiles={smi_enc}&Threshold={threshold}"
    )

    text = pubchem_get(url, return_json=False)
    if text is None:
        return []

    try:
        return [int(x) for x in text.split()]
    except ValueError:
        print("[Error] Could not parse CID list.")
        return []


def pubchem_fastidentity(
    smiles: str,
    identity_type: str = "same_connectivity",
    method: str = "post",
) -> List[int]:
    """
    Perform a PubChem fast identity search for a SMILES string.

    Parameters
    ----------
    smiles : str
        SMILES string to search.
    identity_type : str, default="same_connectivity"
        Identity relationship type (e.g., same_parent, same_scaffold).
    method : {"post", "get"}, default="post"
        HTTP method to use. GET can be used if POST is unstable.

    Returns
    -------
    list[int]
        List of matching PubChem CIDs.
    """
    if not isinstance(smiles, str) or not smiles.strip():
        print("[Error] Invalid SMILES input.")
        return []

    if method.lower() == "get":
        smi_enc = quote(smiles)
        url = (
            f"{PUG_BASE}/compound/fastidentity/smiles/cids/txt"
            f"?smiles={smi_enc}&identity_type={identity_type}"
        )
        text = pubchem_get(url, return_json=False)

    else:
        url = (
            f"{PUG_BASE}/compound/fastidentity/smiles/cids/txt"
            f"?identity_type={identity_type}"
        )
        payload = {"smiles": smiles}
        text = pubchem_post(url, payload=payload, return_json=False)

    if text is None:
        return []

    try:
        return [int(x) for x in text.split()]
    except ValueError:
        print("[Error] Could not parse CID list.")
        return []


# ============================================================
# Exported Names
# ============================================================

__all__ = [
    "pubchem_fastsimilarity",
    "pubchem_fastidentity",
]
