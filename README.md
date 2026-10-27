# Ship Hatch-Corner Structural Optimization

**Parametric finite element modeling · Submodeling · Multi-Island Genetic Algorithm**

Shanghai Jiao Tong University · Undergraduate Research Plan (PRP), 42nd cohort · **September 2022 – September 2023**

> **Interactive web demo:** [Open Hatch-Corner Optimization Lab](https://choppa129.github.io/Ship-Hatch-Corner-Optimization/) — adjust elliptical corner parameters and view original FEA stress figures. If not live, enable **GitHub Settings → Pages → Deploy from a branch → main /docs**. The browser demo is a geometry visualization and does not calculate FEA stress.

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

## Original finite-element figures

The following are **original figures from the SJTU PRP research**, not AI-generated images or outputs from the simplified Python demonstration in this repository. The image files are currently hosted in the companion [personal portfolio repository](https://github.com/choppa129/choppa129.github.io/tree/main/assets).

### 1. Full ship-deck finite-element model

![Original ship deck hatch-opening finite-element model](https://raw.githubusercontent.com/choppa129/choppa129.github.io/main/assets/FEA%E5%8E%9F%E5%A7%8B%E5%AE%8C%E6%95%B4%E7%BB%93%E6%9E%84%E5%9B%BE.png)

*Global finite-element model with the hatch opening and surrounding deck structure.*

### 2. Local hatch-corner parameterization

![Parameterized local hatch corner finite-element mesh](https://raw.githubusercontent.com/choppa129/choppa129.github.io/main/assets/fea%E5%B1%80%E9%83%A8%E7%BB%93%E6%9E%84.png)

*Local corner submodel showing the mesh and geometric parameters L11, L21, len1 and len2.*

### 3. Before vs. after optimization

| Initial design — 534 MPa | Optimized design — 424 MPa |
|:---:|:---:|
| ![Initial von Mises stress contour](https://raw.githubusercontent.com/choppa129/choppa129.github.io/main/assets/%E4%BC%98%E5%8C%96%E5%89%8D.png) | ![Optimized von Mises stress contour](https://raw.githubusercontent.com/choppa129/choppa129.github.io/main/assets/%E4%BC%98%E5%8C%96%E5%90%8E.png) |

The report states a **20.6% reduction in maximum von Mises stress**, from 534 MPa to 424 MPa, for the illustrated hatch-corner shape-optimization case. The figures are original commercial-solver outputs; these values were **not** generated by the independent Python example.

**Image provenance:** SJTU PRP report T010PRP42006 (2022–2023), original FE model and optimization-result figures. The README embeds the images from the personal website repository so they display directly on GitHub; moving or renaming those source assets will break the images.

## Technology

`MSC Patran` · `Patran Command Language (PCL)` · `MSC Nastran` · `Dassault Systèmes Isight` · `Multi-Island Genetic Algorithm (MIGA)` · `Finite Element Analysis` · `Submodeling`

## Research attribution

**Xue Jiang (蒋雪)** — participating student; research report authored in the PRP project.

**Yixuan He (何奕萱)** — participating student and fellow report contributor.

**Jinju Cui (崔进举)** — project supervisor and faculty advisor.

This was collaborative undergraduate research at the School of Naval Architecture, Ocean and Civil Engineering, Shanghai Jiao Tong University. Individual implementation ownership cannot be independently determined from the report alone.

## Run the independent Python demo

The repository now includes an installable **educational 2D finite-element model** in `src/hatchopt/`, a simple multi-island evolutionary optimizer, a CLI and smoke tests. These files are new, independently authored demonstration code—not recovered Patran/Nastran/Isight project files.

```bash
python -m pip install -e ".[dev]"
python -m pytest -q
hatchopt --a 1200 --b 850 --out outputs
hatchopt --optimize --generations 12 --out outputs
```

Outputs: `outputs/stress.png`, `outputs/summary.json` and, when optimizing, `outputs/optimization.json`. The model uses a 2D quarter-domain with an elliptical cutout, plane-stress linear triangles, prescribed displacement and a 2D area proxy for mass. Its numerical values **must not** be compared as a validated reproduction of the original report's 534 → 424 MPa result. See [REPRODUCTION.md](REPRODUCTION.md).

## Reproducibility and limitations

**Research archive with an independent runnable educational demo.** The supplied source is a **research paper, not the original executable PCL scripts, Nastran model, Isight workflow files, mesh or raw simulation results**. The Python example is a different simplified model and does not reproduce the commercial solver implementation. The numerical results above are as reported, not recomputed.

Original title: **集装箱船舱口角隅结构拓扑优化** · Project number **T010PRP42006** · PRP (42nd cohort), 2022–2023.

---
[Robotics & Engineering Portfolio](https://choppa129.github.io/)
