"""Exact Chapter 14 model checks. Requires SymPy; not a mathematical proof checker."""
from itertools import combinations
import sympy as s

passed = []

def clean(a):
    return {i: s.simplify(c) for i,c in a.items() if s.simplify(c) != 0}

def add(*terms):
    result = {}
    for a in terms:
        for i,c in a.items():result[i] = result.get(i,0)+c
    return clean(result)

def scale(a,c):return clean({i:c*v for i,v in a.items()})

def wedge(a,b):
    result = {}
    for i,c in a.items():
        for j,d in b.items():
            if set(i)&set(j):continue
            sign=(-1)**sum(x>y for x in i for y in j)
            k=tuple(sorted(i+j));result[k]=result.get(k,0)+sign*c*d
    return clean(result)

def star(a,metric,volume=None):
    n=len(metric);volume=s.sqrt(s.prod(metric)) if volume is None else volume
    result={}
    for i,c in a.items():
        j=tuple(x for x in range(n) if x not in i)
        sign=(-1)**sum(x>y for x in i for y in j)
        result[j]=result.get(j,0)+c*sign*volume/s.prod(metric[x] for x in i)
    return clean(result)

def contraction(a,vector):
    result={}
    for i,c in a.items():
        for j,index in enumerate(i):
            k=i[:j]+i[j+1:];result[k]=result.get(k,0)+(-1)**j*vector[index]*c
    return clean(result)

def derivative(a,coordinates):
    result={}
    for i,c in a.items():
        for j,x in enumerate(coordinates):result=add(result,wedge({(j,):s.diff(c,x)},{i:1}))
    return result

def zero(value,name):
    if isinstance(value,dict):ok=not clean(value)
    elif isinstance(value,s.MatrixBase):ok=all(s.simplify(v)==0 for v in value)
    else:ok=s.simplify(value)==0
    if not ok:raise AssertionError(name)
    passed.append(name)

for n in range(1,6):
    metric=tuple(s.Integer(i+2)**2 for i in range(n))
    for k in range(n+1):
        for i in combinations(range(n),k):
            a={i:1}
            zero(add(star(star(a,metric),metric),scale(a,-(-1)**(k*(n-k)))),
                 f'double star n={n} I={i}')

for n in range(1,5):
    metric=tuple(s.Integer(i+2)**2 for i in range(n))
    covector=tuple(s.Integer(i+1) for i in range(n))
    vector=tuple(covector[i]/metric[i] for i in range(n))
    norm=sum(covector[i]**2/metric[i] for i in range(n))
    xi={(i,):v for i,v in enumerate(covector)}
    for k in range(n+1):
        for i in combinations(range(n),k):
            a={i:1}
            zero(add(contraction(wedge(xi,a),vector),wedge(xi,contraction(a,vector)),
                     scale(a,-norm)),f'Clifford symbol n={n} I={i}')

# Exact and coexact principal-symbol projections of a nonzero Fourier frequency.
xi={(0,):1,(1,):2,(2,):3};v=(1,2,3);lam=s.Integer(14)
for k in (1,2):
    a={i:s.Integer(j+1) for j,i in enumerate(combinations(range(3),k))}
    e=scale(wedge(xi,contraction(a,v)),1/lam)
    c=scale(contraction(wedge(xi,a),v),1/lam)
    zero(add(a,scale(e,-1),scale(c,-1)),f'Fourier splitting degree {k}')
    zero(sum(e.get(i,0)*c.get(i,0) for i in a),f'Fourier orthogonality degree {k}')
    zero(add(scale(wedge(xi,contraction(e,v)),1/lam),scale(e,-1)),
         f'Fourier exact projection degree {k}')

x,y=s.symbols('x y',real=True)
u=s.Function('u',real=True)(x,y);f=s.Function('f',real=True)(x,y)
metric=(s.exp(2*u),s.exp(2*u));volume=s.exp(2*u)
def st(a):return star(a,metric,volume)
def d(a):return derivative(a,(x,y))
def delta(a):return scale(st(d(st(a))),-1)
zero(add(delta(d({():f})),{():s.exp(-2*u)*(s.diff(f,x,2)+s.diff(f,y,2))}),
     'conformal scalar Hodge Laplacian sign')
zero(add(delta({(0,1):s.exp(2*u)*s.cos(x)}),{(1,):-s.sin(x)}),
     'conformal coexact torus potential')

# Derive conformal curvature from Christoffel coefficients, separately from the frame formula.
g=s.diag(*metric);inv=g.inv();coords=(x,y)
Gamma=[[[s.simplify(sum(inv[a,b]*(s.diff(g[j,b],coords[i])+s.diff(g[i,b],coords[j])
         -s.diff(g[i,j],coords[b]))/2 for b in range(2)))
         for j in range(2)] for i in range(2)] for a in range(2)]
R=s.diff(Gamma[0][1][1],x)-s.diff(Gamma[0][0][1],y)+sum(
    Gamma[0][0][j]*Gamma[j][1][1]-Gamma[0][1][j]*Gamma[j][0][1] for j in range(2))
zero(R/g[1,1]+s.exp(-2*u)*(s.diff(u,x,2)+s.diff(u,y,2)),
     'conformal Gaussian curvature from Christoffel symbols')

# Independently compute geodesic curvature at a point on a circular boundary, u=x^2+y^2.
rad=s.symbols('rad',positive=True);point={x:rad,y:0}
Gamma_rad=[[[s.simplify(v.subs(u,x*x+y*y).doit()).subs(point) for v in row]
            for row in plane] for plane in Gamma]
speed=rad*s.exp(rad**2)
T=s.Matrix([0,s.exp(-rad**2)])
ordinary_acc=s.Matrix([-s.exp(-2*rad**2)/rad,0])
acc=ordinary_acc+s.Matrix([sum(Gamma_rad[a][i][j]*T[i]*T[j]
                              for i in range(2) for j in range(2)) for a in range(2)])
left=s.Matrix([-s.exp(-rad**2),0])
kg=s.simplify(s.exp(2*rad**2)*acc.dot(left))
zero(2*s.pi*speed*kg-2*s.pi*(1+2*rad**2),'outer circular boundary integral')
r0,R0=s.symbols('r0 R0',positive=True)
zero(-4*s.pi*(R0**2-r0**2)+2*s.pi*(1+2*R0**2)-2*s.pi*(1+2*r0**2),
     'annulus curvature and both oriented boundaries')

theta,theta0,R=s.symbols('theta theta0 R',positive=True)
poisson=-s.diff(s.sin(theta)*s.diff(R**2*s.cos(theta)/2,theta),theta)/(R**2*s.sin(theta))
zero(poisson-s.cos(theta),'spherical Poisson equation')
zero(s.integrate(2*s.pi*s.sin(theta),(theta,0,theta0))+2*s.pi*s.cos(theta0)-2*s.pi,
     'spherical cap curvature and geodesic boundary')
zero((3*s.pi/2-s.pi)-s.pi/2,'spherical octant angle excess')

def pf4(omega):
    return add(wedge(omega[0][1],omega[2][3]),
               scale(wedge(omega[0][2],omega[1][3]),-1),
               wedge(omega[0][3],omega[1][2]))

K,K1,K2=s.symbols('K K1 K2',real=True)
omega=[[{} for _ in range(4)] for _ in range(4)]
for i in range(4):
    for j in range(i+1,4):omega[i][j]={(i,j):K};omega[j][i]={(i,j):-K}
zero(add(pf4(omega),{(0,1,2,3):-3*K*K}),'four-dimensional constant-curvature Pfaffian')
product=[[{} for _ in range(4)] for _ in range(4)]
product[0][1]={(0,1):K1};product[1][0]={(0,1):-K1}
product[2][3]={(2,3):K2};product[3][2]={(2,3):-K2}
zero(add(pf4(product),{(0,1,2,3):-K1*K2}),'product curvature Pfaffian')
Q=s.eye(4);Q[0,0]=Q[2,2]=s.Rational(3,5);Q[0,2]=-s.Rational(4,5);Q[2,0]=s.Rational(4,5)
rot=[[add(*(scale(omega[a][b],Q[a,i]*Q[b,j]) for a in range(4) for b in range(4)))
      for j in range(4)] for i in range(4)]
zero(add(pf4(rot),scale(pf4(omega),-1)),'Pfaffian invariant under oriented orthogonal frame change')
zero((4*s.pi*R0**2)*(4*s.pi*r0**2)/(4*s.pi**2*R0**2*r0**2)-4,
     'product of two spheres Euler-form integral')
print(f'PASS: {len(passed)} exact model identities; not an independent mathematical review.')
