# Ship Hatch-Corner Structural Optimization

**Parametric finite element modeling · Submodeling · Multi-Island Genetic Algorithm**

Shanghai Jiao Tong University · Undergraduate Research Plan (PRP), 42nd cohort · **September 2022 – September 2023**

## Results at a glance

| Metric | Initial | Optimized |
|---|---:|---:|
| Maximum von Mises stress (case study) | **534 MPa** | **424 MPa** |
| Reduction in peak stress | — | **20.6%** |
| Elliptical hatch-corner design variables | Initial parameters documented in the report | **a = 1386 mm; b = 1354 mm** |

The report describes reducing stress concentration around a container ship's hatch opening corner using **parameterized geometry and finite element analysis (FEA)** followed by **multi-island genetic algorithm (MIGA)** optimization in Isight. The reported stress decrease is from a specific shape-optimization case study; it is not a general guarantee for other loading cases or ship geometries.

> **Terminology:** The original PRP report is titled *Topology Optimization of Container-Ship Hatch Corner Structures* (集装箱船舱口角隅结构拓扑优化). The demonstrated numerical case varies the geometry of an elliptical corner; more precisely, it is a **structural shape-optimization** example under the wider theme of structural optimization.

## Engineering challenge

Hatch openings introduce geometric discontinuities in ship deck structures that concentrate stress. Optimizing an entire ship model at fine resolution is expensive. This research investigated a **global–local submodeling workflow** to evaluate and optimize the local hatch-corner geometry while incorporating boundary displacements from a larger finite element model.

## Methodology

1. **Parameterized geometry:** Used Patran's PCL-based workflow to define geometric variables, generate/update models and meshes, and automate aspects of finite-element analysis.
2. **Global–local submodeling:** Extracted a local hatch-corner submodel from the larger hull/deck model; transferred displacement boundary conditions from the global model and refined the local mesh.
3. **FEA-driven optimization:** Coupled Patran/Nastran calculations with Isight to evaluate design candidates and perform a multi-island genetic algorithm search.
4. **Candidate evaluation:** Compared the initial and optimized von Mises stress distributions and evaluated shape parameters under design and mass constraints.

### Optimization setup (reported illustrative case)

- **Objective:** Minimize the maximum von Mises stress.
- **Design variables:** Elliptical hatch-corner semi-axis/shape parameters `a` and `b`.
- **Search bounds documented for the case:** `1000 mm ≤ a ≤ 1400 mm` and `500 mm ≤ b ≤ 2000 mm`.
- **Reported MIGA solution:** `a = 1386 mm`, `b = 1354 mm`.
- **Reported maximum stress:** `534 MPa → 424 MPa` (**20.6% reduction**).

The paper discusses additional multi-condition stress and mass constraints. They are not claimed here as a separately reproduced optimization run.

## Research figures and source materials

The original research report includes **real simulation results** rather than generated artwork. Particularly useful figures include:

- **Submodel FE stress distribution and model comparisons** — report pp. 5–6 and 16–17.
- **Isight optimization workflow** — report p. 7.
- **Initial vs optimized von Mises stress distributions** — report pp. 8 and 20.

The report is available from the author's original PRP research files. The document is not embedded in this repo until the author has reviewed its public-release contents and collaborators' details. For a faithful portfolio figure gallery, publish selected, cropped original figures with captions and source-page citations—not synthetic visualizations.

## Technology

`MSC Patran` · `Patran Command Language (PCL)` · `MSC Nastran` · `Dassault Systèmes Isight` · `Multi-Island Genetic Algorithm (MIGA)` · `Finite Element Analysis` · `Submodeling`

## Research attribution

**Xue Jiang (蒋雪)** — participating student; research report authored in the PRP project.

**Yixuan He (何奕萱)** — participating student and fellow report contributor.

**Jinju Cui (崔进举)** — project supervisor and faculty advisor.

This was collaborative undergraduate research at the School of Naval Architecture, Ocean and Civil Engineering, Shanghai Jiao Tong University. Individual implementation ownership cannot be independently determined from the report alone.

## Reproducibility and limitations

**Documentation-based research archive.** The supplied source is a **research paper, not the original executable PCL scripts, Nastran model, Isight workflow files, mesh or raw simulation results**. This repository therefore does not claim a push-button reproducible solver implementation. The numerical results above are as reported, not recomputed.

Original title: **集装箱船舱口角隅结构拓扑优化** · Project number **T010PRP42006** · PRP (42nd cohort), 2022–2023.

---
[Robotics & Engineering Portfolio](https://choppa129.github.io/)
