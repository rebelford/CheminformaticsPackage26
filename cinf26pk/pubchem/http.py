"""
HTTP utilities for interacting with the PubChem PUG-REST API.

This module provides low-level, reusable HTTP helper functions with
retry and exponential backoff logic. These functions are intentionally
domain-agnostic and do not interpret PubChem-specific responses.

Functions
---------
- pubchem_get : Safe GET request with retries
- pubchem_post : Safe POST request with retries
"""

# ============================================================
# Imports
# ============================================================

import time
import requests

# ============================================================
# Constants
# ============================================================

DEFAULT_RETRIES = 3
DEFAULT_TIMEOUT = 30

# ============================================================
# HTTP Helper Functions
# ============================================================

def pubchem_post(
    url: str,
    payload: dict | None = None,
    retries: int = DEFAULT_RETRIES,
    timeout: int = DEFAULT_TIMEOUT,
    base_delay: int = 2,
    return_json: bool = True,
):
    """
    Safely perform a POST request with retry and exponential backoff.

    Parameters
    ----------
    url : str
        Full PubChem POST endpoint.
    payload : dict, optional
        JSON payload for the POST request.
    retries : int
        Number of retry attempts.
    timeout : int
        Timeout (seconds) for each request.
    base_delay : int
        Base delay for exponential backoff.
    return_json : bool
        If True, return parsed JSON; otherwise return raw text.

    Returns
    -------
    dict | str | None
        Parsed response, raw text, or None if all attempts fail.
    """
    for attempt in range(1, retries + 1):
        try:
            r = requests.post(url, json=payload, timeout=timeout)
            r.raise_for_status()
            return r.json() if return_json else r.text

        except Exception as e:
            print(f"[Warning] POST attempt {attempt}/{retries} failed")
            print(f"         URL: {url}")
            print(f"         Error: {type(e).__name__}: {e}")
            time.sleep(base_delay * attempt)

    print(f"[Error] All POST attempts failed for URL: {url}")
    return None


def pubchem_get(
    url: str,
    retries: int = DEFAULT_RETRIES,
    timeout: int = DEFAULT_TIMEOUT,
    base_delay: int = 2,
    return_json: bool = True,
):
    """
    Safely perform a GET request with retry and exponential backoff.

    Parameters
    ----------
    url : str
        Full URL for the GET request.
    retries : int
        Number of retry attempts.
    timeout : int
        Timeout (seconds) for request.
    base_delay : int
        Base delay for exponential backoff.
    return_json : bool
        If True, return parsed JSON; otherwise return raw text.

    Returns
    -------
    dict | str | None
        Parsed response, raw text, or None if all attempts fail.
    """
    for attempt in range(1, retries + 1):
        try:
            r = requests.get(url, timeout=timeout)
            r.raise_for_status()
            return r.json() if return_json else r.text

        except Exception as e:
            print(f"[Warning] GET attempt {attempt}/{retries} failed")
            print(f"         URL: {url}")
            print(f"         Error: {type(e).__name__}: {e}")
            time.sleep(base_delay * attempt)

    print(f"[Error] All GET attempts failed for URL: {url}")
    return None


# ============================================================
# Exported Names
# ============================================================

__all__ = ["pubchem_get", "pubchem_post"]
