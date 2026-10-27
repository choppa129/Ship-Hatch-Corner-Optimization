import argparse
import json
from pathlib import Path
from .model import solve
from .optimizer import optimize


def main():
    p=argparse.ArgumentParser(description='Illustrative 2-D hatch corner FE model')
    p.add_argument('--optimize',action='store_true')
    p.add_argument('--a',type=float,default=1200)
    p.add_argument('--b',type=float,default=850)
    p.add_argument('--generations',type=int,default=12)
    p.add_argument('--out',default='outputs')
    args=p.parse_args()
    outdir=Path(args.out);outdir.mkdir(parents=True,exist_ok=True)
    if args.optimize:
        result=optimize(generations=args.generations)
        a,b=result.a_mm,result.b_mm
        (outdir/'optimization.json').write_text(json.dumps(result.__dict__,indent=2))
    else: a,b=args.a,args.b
    result=solve(a,b)
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from matplotlib.tri import Triangulation
    tri=Triangulation(result['nodes'][:,0],result['nodes'][:,1],result['triangles'])
    fig,ax=plt.subplots(figsize=(8,6))
    pc=ax.tripcolor(tri,facecolors=result['von_mises_mpa'],shading='flat',cmap='viridis')
    fig.colorbar(pc,ax=ax,label='von Mises stress (MPa)')
    ax.set_aspect('equal');ax.set(xlabel='x (mm)',ylabel='y (mm)',title=f'Illustrative 2D FEM: a={a:.1f}, b={b:.1f} mm')
    fig.tight_layout();fig.savefig(outdir/'stress.png',dpi=160);plt.close(fig)
    summary={'a_mm':a,'b_mm':b,'max_von_mises_mpa':result['max_von_mises_mpa'],'area_mm2':result['area_mm2'],
             'disclaimer':'Illustrative 2D FE model; not original paper result or validated ship analysis'}
    (outdir/'summary.json').write_text(json.dumps(summary,indent=2))
    print(json.dumps(summary,indent=2))

if __name__=='__main__': main()
