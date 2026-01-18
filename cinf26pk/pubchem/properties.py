"""
PubChem compound property retrieval utilities.

This module provides high-level functions for retrieving compound
properties from the PubChem PUG-REST API for large CID lists using
chunked requests and rate limiting.

Functions
---------
- pubchem_properties_for_cids : Retrieve compound properties as CSV text
"""

# ============================================================
# Imports
# ============================================================

import time
from math import ceil
from typing import List, Tuple

from tqdm import tqdm

from .http import pubchem_get

# ============================================================
# Constants
# ============================================================

PUG_BASE = "https://pubchem.ncbi.nlm.nih.gov/rest/pug"

# ============================================================
# Property Retrieval (Batch CSV)
# ============================================================

def pubchem_properties_for_cids(
    cid_list: List[int],
    properties: List[str] | None = None,
    chunk_size: int = 100,
    sleep_time: float = 0.25,
) -> Tuple[str, List[int]]:
    """
    Retrieve PubChem compound properties for large lists of CIDs using
    chunked API requests.

    Parameters
    ----------
    cid_list : list[int]
        List of PubChem compound IDs (CIDs).
    properties : list[str], optional
        Property fields to request. If None, a default set is used.
    chunk_size : int, default=100
        Number of CIDs per API request.
    sleep_time : float, default=0.25
        Delay (seconds) between API calls to reduce rate limiting.

    Returns
    -------
    csv_text : str
        Combined CSV output containing all requested properties.
    failed_chunks : list[int]
        Indices of CID chunks that failed to retrieve.
    """
    if not cid_list:
        print("[Warning] No CIDs provided.")
        return "", []

    if properties is None:
        properties = [
            "HBondDonorCount",
            "HBondAcceptorCount",
            "MolecularWeight",
            "XLogP",
            "ConnectivitySMILES",
            "SMILES",
        ]

    num_chunks = ceil(len(cid_list) / chunk_size)
    failed_chunks: List[int] = []
    csv_output = ""

    print(f"# CIDs: {len(cid_list)}, chunks: {num_chunks}")

    prop_str = ",".join(properties)

    for i in tqdm(range(num_chunks), desc="Retrieving PubChem properties"):
        chunk = cid_list[i * chunk_size : (i + 1) * chunk_size]
        cid_str = ",".join(map(str, chunk))

        url = f"{PUG_BASE}/compound/cid/{cid_str}/property/{prop_str}/csv"

        text = pubchem_get(url, return_json=False)
        if text is None:
            failed_chunks.append(i)
            continue

        lines = text.splitlines()
        if i == 0:
            csv_output = "\n".join(lines)
        else:
            csv_output += "\n" + "\n".join(lines[1:])  # skip header

        time.sleep(sleep_time)

    return csv_output, failed_chunks


# ============================================================
# Exported Names
# ============================================================

__all__ = ["pubchem_properties_for_cids"]
