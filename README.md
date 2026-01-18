# cinf26pk

**cinf26pk** is a lightweight Python package used throughout the
*2026 Cheminformatics* course to support reproducible data workflows,
PubChem access, and module-specific utilities.

This package is designed for **educational use** and prioritizes:
- clarity over cleverness
- explicit structure
- reproducible filesystem conventions

---

## Package Structure

The package is organized into clear subpackages:

- `cinf26pk.c python ore`  
  General-purpose utilities shared across the course
  (filenames, I/O helpers, small utilities)

- `cinf26pk.pubchem`  
  High-level wrappers for interacting with the PubChem PUG-REST API
  (search, property retrieval, robust HTTP access)

- `cinf26pk.mod10`  
  Module 10 (Supervised Machine Learning) helpers
  (canonical filesystem paths, shared definitions)

---

## Installation (Editable Mode)

Activate your course environment, then install the package in editable
mode from the directory containing `pyproject.toml`:

```bash
pip install -e .
```