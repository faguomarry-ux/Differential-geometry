"""Symbolic cross-checks of Chapter 13 examples; requires SymPy, not a proof checker.

Run from the repository root with a Python environment containing SymPy.
The geometry is calculated from immersion derivatives or orthogonal projections.
"""
import sympy as s

checks = []

def zero(value, name):
    entries = list(value) if isinstance(value, s.MatrixBase) else [value]
    assert all(s.simplify(x) == 0 for x in entries), name
    checks.append(name)

def geometry(F, coordinates):
    J = F.jacobian(coordinates)
    g = s.simplify(J.T * J)
    inv = s.simplify(g.inv())
    m = len(coordinates)
    Gamma = [[[s.simplify(sum(inv[k,l] * (
        s.diff(g[j,l], coordinates[i]) + s.diff(g[i,l], coordinates[j])
        - s.diff(g[i,j], coordinates[l])) / 2 for l in range(m)))
        for j in range(m)] for i in range(m)] for k in range(m)]
    B = [[s.simplify(F.diff(coordinates[i], coordinates[j]) -
          sum((J[:, k] * Gamma[k][i][j] for k in range(m)), s.zeros(len(F),1)))
          for j in range(m)] for i in range(m)]
    H = s.simplify(sum((inv[i,j] * B[i][j] for i in range(m) for j in range(m)),
                       s.zeros(len(F),1)) / m)
    return J, g, inv, Gamma, B, H

x,y = s.symbols('x y', real=True)
F = s.Matrix([x,y,(x*x-y*y)/2,x*y])
J,g,inv,G,B,H = geometry(F, (x,y))
zero(g-(1+x*x+y*y)*s.eye(2), 'codimension-two induced metric')
zero(H, 'codimension-two mean curvature from projected second derivatives')
for i in range(2):
    for j in range(2):
        zero(J.T * B[i][j], f'B({i},{j}) normal')
coords=(x,y)
for i in range(2):
    for j in range(2):
        for k in range(2):
            for l in range(2):
                R = sum(g[l,a] * (s.diff(G[a][j][k],coords[i])
                    - s.diff(G[a][i][k],coords[j])
                    + sum(G[a][i][b]*G[b][j][k] - G[a][j][b]*G[b][i][k]
                          for b in range(2))) for a in range(2))
                rhs = B[i][l].dot(B[j][k]) - B[j][l].dot(B[i][k])
                zero(R-rhs, f'Gauss component {i}{j}{k}{l}')
P=s.simplify(s.eye(4)-J*inv*J.T)
for i in range(2):
    for j in range(2):
        for k in range(2):
            def cov(a,b,c):
                return P*B[b][c].diff(coords[a])-sum((
                    G[d][a][b]*B[d][c]+G[d][a][c]*B[b][d]
                    for d in range(2)),s.zeros(4,1))
            zero(cov(i,j,k)-cov(j,i,k), f'normal Codazzi {i}{j}{k}')
# Curvature of the normal subbundle calculated directly from its projector.
normal_R=s.simplify(P*(P.diff(x)*P.diff(y)-P.diff(y)*P.diff(x))*P)
zero(normal_R[3,2].subs({x:0,y:0})+2, 'normal projector curvature sign -2')
A1=s.Matrix([[1,0],[0,-1]]);A2=s.Matrix([[0,1],[1,0]])
zero((A1*A2-A2*A1)[1,0]+2, 'Ricci commutator sign -2')

u,v=s.symbols('u v',real=True)
c=s.symbols('c',positive=True)
F=s.Matrix([u*s.cos(v),u*s.sin(v),c*v])
J,g,inv,G,B,H=geometry(F,(u,v))
zero(H,'helicoid mean curvature')
n=s.Matrix([c*s.sin(v),-c*s.cos(v),u])/s.sqrt(u*u+c*c)
b=s.Matrix(2,2,lambda i,j:s.simplify(B[i][j].dot(n)))
zero(b[0,1]+c/s.sqrt(u*u+c*c),'helicoid mixed second form sign')
zero(b.det()/g.det()+c*c/(u*u+c*c)**2,'helicoid Gaussian curvature')

F=s.Matrix([s.cos(u),s.sin(u),s.cos(v),s.sin(v)])/s.sqrt(2)
J,g,inv,G,B,H=geometry(F,(u,v))
zero(g-s.eye(2)/2,'Clifford torus induced metric')
zero(H+F,'Clifford Euclidean mean curvature -F')
Bs=[[s.simplify(B[i][j]+g[i,j]*F) for j in range(2)] for i in range(2)]
zero(sum((inv[i,j]*Bs[i][j] for i in range(2) for j in range(2)),s.zeros(4,1)),
     'Clifford spherical mean curvature zero')
n=s.Matrix([s.cos(u),s.sin(u),-s.cos(v),-s.sin(v)])/s.sqrt(2)
shape=s.simplify(inv*s.Matrix(2,2,lambda i,j:Bs[i][j].dot(n)))
zero(shape-s.diag(-1,1),'Clifford spherical principal signs')

# Sphere outward variation: derivative of local volume factor agrees with -m H.
a,t=s.symbols('a t',positive=True)
for m in (1,2,3,5):
    zero(s.diff((a+t)**m,t).subs(t,0)-m*a**(m-1),f'sphere volume variation m={m}')
zero(s.diff(-s.cos(x),x)-s.sin(x),'sphere moving-frame curvature sign')

# Compare the graph Euler-Lagrange expression with the trace of its second form.
f=s.Function('f')(x,y);p=s.Matrix([s.diff(f,x),s.diff(f,y)])
W=s.sqrt(1+(p.T*p)[0]);hess=s.hessian(f,(x,y))
trace=s.trace((s.eye(2)-p*p.T/W**2)*hess)/W
zero(s.diff(p[0]/W,x)+s.diff(p[1]/W,y)-trace,'minimal graph divergence identity')
rho=s.symbols('rho',real=True)
L=s.sqrt(1+x*x+y*y)
zero(s.hessian(L,(x,y))-(s.eye(2)/L-s.Matrix([x,y])*s.Matrix([[x,y]])/L**3),
     'graph area integrand convex Hessian')
print(f'PASS: {len(checks)} symbolic model identities; not an independent mathematical review.')
