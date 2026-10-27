"""Simple reproducible multi-island genetic algorithm demonstration."""
from dataclasses import dataclass
import numpy as np
from .model import solve

BOUNDS = np.array([[1000.,1400.],[500.,2000.]])

@dataclass
class Result:
    a_mm: float
    b_mm: float
    objective_mpa: float
    history: list


def optimize(generations=12, islands=3, population=8, seed=42,
             mesh_theta=16, mesh_radial=7, max_area_ratio=1.005):
    """Minimize FEM max von Mises with a material-area constraint.

    Multiple evolving subpopulations with periodic migration. NOT Isight MIGA.
    Area is a 2-D proxy, not vessel structural mass.
    """
    if population < 4 or islands < 1 or generations < 1:
        raise ValueError('population>=4, islands>=1, generations>=1 required')
    rng=np.random.default_rng(seed)
    reference=solve(1200,850,n_theta=mesh_theta,n_radial=mesh_radial)['area_mm2']
    cache={}
    def score(v):
        key=tuple(np.round(v,3))
        if key not in cache:
            out=solve(*v,n_theta=mesh_theta,n_radial=mesh_radial)
            penalty=max(0.,out['area_mm2']/reference-max_area_ratio)*100000
            cache[key]=out['max_von_mises_mpa']+penalty
        return cache[key]
    pools=[rng.uniform(BOUNDS[:,0],BOUNDS[:,1],size=(population,2)) for _ in range(islands)]
    history=[]
    for gen in range(generations):
        for k,pool in enumerate(pools):
            ranked=sorted(pool,key=score)
            elites=np.array(ranked[:max(2,population//3)])
            offspring=[v.copy() for v in elites]
            while len(offspring)<population:
                p1,p2=elites[rng.integers(len(elites),size=2)]
                child=(p1+p2)/2 + rng.normal(0,[22,85])
                offspring.append(np.clip(child,BOUNDS[:,0],BOUNDS[:,1]))
            pools[k]=np.array(offspring)
        if islands>1 and (gen+1)%4==0:
            migrants=[min(pool,key=score).copy() for pool in pools]
            for k in range(islands): pools[(k+1)%islands][-1]=migrants[k]
        best=min((v for pool in pools for v in pool),key=score)
        history.append({'generation':gen+1,'best_objective_mpa':float(score(best))})
    best=min((v for pool in pools for v in pool),key=score)
    return Result(float(best[0]),float(best[1]),float(score(best)),history)
