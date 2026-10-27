# Open-source reproduction code

A standalone Python implementation of a **2D plane-stress finite-element model** with a quarter-elliptical cutout and an illustrative multi-island genetic optimizer has been prepared separately as a source ZIP.

The code includes mesh generation, constant-strain triangle stiffness assembly, sparse solution, von Mises stress visualization, a multi-island evolutionary search, CLI and tests.

**Important:** This is an independent educational model. It is **not** the original Patran/Nastran/Isight implementation, does not reproduce the original vessel submodel or boundary conditions, and must not be represented as a reproduction of the paper's 534 to 424 MPa results. The example's output depends on its assumed geometry, far-field displacement and material parameters.

To integrate, add the source files from the generated archive to this repository and follow its README. Original commercial solver inputs remain unavailable.
