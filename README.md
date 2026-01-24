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

- `cinf26pk.core`  
  General-purpose utilities shared across the course  
  (filenames, I/O helpers, small utilities)

- `cinf26pk.pubchem`  
  High-level wrappers for interacting with the PubChem PUG-REST API  
  (search, property retrieval, robust HTTP access)

- `cinf26pk.mod10`  
  Module-specific helpers for supervised machine learning

---

## Important Workflow Note (Please Read)

This repository contains **course-maintained package code**.

- **Do not edit files in this repository**
- You will receive updates during the semester using `git pull`
- Your own notebooks and scripts should live in a **separate directory**

This avoids merge conflicts and ensures everyone is running the same
package code.

Editable installation allows you to use this package from anywhere
without copying files.

---

## Installation (Recommended: Editable Mode)

### Step 1. Clone the repository

```bash
git clone https://github.com/rebelford/CheminformaticsPackage26.git
cd CheminformaticsPackage26
cheminformaticsPackage26
```
### Step 2: activate your course environment
#### If you are using a Conda Environment
```bash
conda activate cinf26
```
#### If you are using a virtual environment (venv)
Inside the repo directory 
```bash
python -m venv .venv
```
this creates a `cheminformaticsPackage26/.venv/` subdirectory, and then run
```bash
source .venv/bin/activate
```
you should see something like `(.venv) user@machine:CheminformaticsPackage26$`
`
### Step 3: Install the package in editable mode
```bash
pip install -e .
```

## Update package during the semester
You should not edit any of these files during the semester or you may have merge conflicts when you pull updates from the repo
### Step 1: Navigate to the cloned repo
```bash
cd CheminformaticsPackage26
```
### Step 2: Pull the latest changes
```bash
git pull
```
Because the package was installed in editable mode, the updated code is available immediately the next time Python is run or the Jupyter kernel is restarted.

