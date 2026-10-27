"""Illustrative 2-D plane-stress FEM for a quarter-elliptical cutout.

Independent demonstration, NOT the original Patran/Nastran ship model.
"""
import numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import spsolve


def mesh(a_mm: float, b_mm: float, n_theta: int = 28, n_radial: int = 12, outer_radius_mm: float = 4000):
    """Quarter annulus with an elliptical inner boundary and circular outer boundary."""
    if not (0 < a_mm < outer_radius_mm and 0 < b_mm < outer_radius_mm):
        raise ValueError('a and b must be between zero and outer_radius_mm')
    theta = np.linspace(0, np.pi / 2, n_theta + 1)
    rho = np.linspace(0, 1, n_radial + 1)
    points = []
    for t in theta:
        inner = 1.0 / np.sqrt((np.cos(t) / a_mm) ** 2 + (np.sin(t) / b_mm) ** 2)
        for q in rho:
            radius = inner + q * (outer_radius_mm - inner)
            points.append([radius * np.cos(t), radius * np.sin(t)])
    nodes = np.asarray(points, float)
    tris = []
    stride = n_radial + 1
    for i in range(n_theta):
        for j in range(n_radial):
            p = i * stride + j
            tris.extend([(p, p + 1, p + stride), (p + stride, p + 1, p + stride + 1)])
    return nodes, np.asarray(tris, int), stride


def solve(a_mm: float, b_mm: float, n_theta: int = 28, n_radial: int = 12,
          outer_radius_mm: float = 4000, E_mpa: float = 210000, nu: float = 0.3,
          applied_strain: float = 0.001):
    """CST plane-stress FEM with prescribed illustrative far-field displacement.

    Outer circular boundary: ux=eps*x, uy=0; x=0 symmetry ux=0;
    y=0 symmetry uy=0. Inner elliptical edge is traction free.
    No ship-specific loads or shell/plate bending are represented.
    """
    nodes, triangles, stride = mesh(a_mm, b_mm, n_theta, n_radial, outer_radius_mm)
    D = E_mpa / (1 - nu ** 2) * np.array([[1, nu, 0], [nu, 1, 0], [0, 0, (1 - nu) / 2]])
    rows, cols, vals = [], [], []
    Bs, areas = [], []
    for tri in triangles:
        p = nodes[tri]
        x1, y1 = p[0]; x2, y2 = p[1]; x3, y3 = p[2]
        det = (x2-x1)*(y3-y1)-(x3-x1)*(y2-y1)
        if det <= 0: raise ValueError('Invalid mesh element orientation')
        area = det / 2
        B = np.array([[y2-y3,0,y3-y1,0,y1-y2,0],
                      [0,x3-x2,0,x1-x3,0,x2-x1],
                      [x3-x2,y2-y3,x1-x3,y3-y1,x2-x1,y1-y2]]) / det
        ke = area * B.T @ D @ B
        dof = np.column_stack([2*tri, 2*tri+1]).ravel()
        rows.extend(np.repeat(dof,6)); cols.extend(np.tile(dof,6)); vals.extend(ke.ravel())
        Bs.append(B); areas.append(area)
    n = len(nodes)*2
    K = coo_matrix((vals,(rows,cols)),shape=(n,n)).tocsr()
    fixed = {}
    for k,(x,y) in enumerate(nodes):
        if abs(x) < 1e-7: fixed[2*k] = 0.0
        if abs(y) < 1e-7: fixed[2*k+1] = 0.0
    for i in range(n_theta+1):
        k = i*stride + n_radial
        fixed[2*k] = applied_strain*nodes[k,0]
        fixed[2*k+1] = 0.0
    fixed_ids = np.array(sorted(fixed),int)
    u = np.zeros(n)
    u[fixed_ids] = np.array([fixed[j] for j in fixed_ids])
    free = np.setdiff1d(np.arange(n),fixed_ids)
    u[free] = spsolve(K[free][:,free], -(K[free][:,fixed_ids] @ u[fixed_ids]))
    stresses = []
    for tri,B in zip(triangles,Bs):
        dof = np.column_stack([2*tri,2*tri+1]).ravel()
        stresses.append(D @ (B @ u[dof]))
    stress = np.asarray(stresses)
    sx, sy, txy = stress.T
    vm = np.sqrt(sx*sx - sx*sy + sy*sy + 3*txy*txy)
    return {'nodes':nodes,'triangles':triangles,'displacements':u.reshape(-1,2),
            'stress_mpa':stress,'von_mises_mpa':vm,'max_von_mises_mpa':float(vm.max()),
            'area_mm2':float(np.sum(areas))}
