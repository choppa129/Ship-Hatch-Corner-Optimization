import numpy as np
from hatchopt import mesh, solve, optimize

def test_mesh():
    nodes,tris,_=mesh(1200,850,n_theta=6,n_radial=3)
    assert nodes.shape==(28,2)
    assert len(tris)==36

def test_fem():
    result=solve(1200,850,n_theta=8,n_radial=4)
    assert np.isfinite(result['von_mises_mpa']).all()
    assert result['max_von_mises_mpa']>0

def test_optimizer():
    result=optimize(generations=1,islands=1,population=4,mesh_theta=6,mesh_radial=3)
    assert 1000<=result.a_mm<=1400
    assert 500<=result.b_mm<=2000
