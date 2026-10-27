# Independent Python FEM reproduction companion

This repository now contains the runnable Python source in `src/hatchopt/`, an installable `pyproject.toml`, and smoke tests in `tests/`.

## Quick start

```bash
python -m pip install -e ".[dev]"
python -m pytest -q
hatchopt --a 1200 --b 850 --out outputs
hatchopt --optimize --generations 12 --out outputs
```

The example builds a **2D quarter-annular plane-stress mesh with an elliptical cutout**, solves a prescribed-displacement FE problem using constant-strain triangles, calculates von Mises stress, and searches `a` and `b` using a seeded multi-island genetic algorithm. It exports a stress PNG and JSON results.

## Not an original solver reproduction

This is an **independently authored educational model**, not the original Patran/Nastran/Isight implementation. It does not reproduce the original ship structure, submodel displacement transfer, shell geometry, loading cases, mesh convergence or mass constraints. The reported **534 → 424 MPa (20.6%)** result belongs to the original research paper, not this Python example.

The optimizer uses a 2D area proxy for mass. Its fitness includes a penalty and should not be interpreted as a measured stress unless evaluated separately. Three smoke tests check mesh sizes, finite stress values and search bounds; they are not a validation study.
