"""Exact Chapter 16 checks from coordinates and matrix derivatives.

Requires SymPy; examples do not replace the general proofs or independent review.
"""
import sympy as s

checks = []


def zero(value, name):
    entries = list(value) if isinstance(value, s.MatrixBase) else [value]
    assert all(s.simplify(s.trigsimp(v)) == 0 for v in entries), name
    checks.append(name)


def bracket(A, B):
    return A*B-B*A


def curvature(A, q, i, j):
    return A[j].diff(q[i])-A[i].diff(q[j])+bracket(A[i], A[j])


x,y,z,u,v,psi = s.symbols('x y z u v psi', real=True)
H=s.diag(1,-1);E=s.Matrix([[0,1],[0,0]]);F=E.T
q=[x,y,z]
A=[y*E,z*H,x*F]
g=(s.eye(2)+x*E)*s.diag(s.exp(y),s.exp(-y))
ginv=g.inv()
B=[s.simplify(ginv*a*g+ginv*g.diff(t)) for a,t in zip(A,q)]
FA={(i,j):curvature(A,q,i,j) for i in range(3) for j in range(i+1,3)}
FB={(i,j):curvature(B,q,i,j) for i in range(3) for j in range(i+1,3)}
for ij,mat in FA.items():
    zero(FB[ij]-ginv*mat*g,f'nonabelian curvature covariance {ij}')
    for vec in [s.Matrix([x+y,z+x*y]),s.Matrix([x*z,y*z])]:
        i,j=ij
        def cov(coeff,field,k):return field.diff(q[k])+coeff[k]*field
        lhs=cov(A,cov(A,vec,j),i)-cov(A,cov(A,vec,i),j)
        zero(lhs-mat*vec,f'associated curvature commutator {ij} {vec[0]}')
for i in range(3):
    field=s.Matrix([x+y*z,x*x-z])
    zero((ginv*field).diff(q[i])+B[i]*ginv*field
         -ginv*(field.diff(q[i])+A[i]*field),f'covariant section transformation {i}')
bianchi=s.zeros(2)
for k,i,j in [(0,1,2),(1,2,0),(2,0,1)]:
    fab=curvature(A,q,i,j)
    bianchi+=fab.diff(q[k])+bracket(A[k],fab)
zero(bianchi,'matrix Bianchi from independent coordinate curvature')

# Explicit two-dimensional exercise, including the often missed wedge term.
g2=s.eye(2)+x*E
A2=[s.zeros(2),x*H]
B2=[s.simplify(g2.inv()*a*g2+g2.inv()*g2.diff(t)) for a,t in zip(A2,[x,y])]
zero(B2[0]-E,'exercise transformed dx coefficient')
zero(B2[1]-x*H-2*x*x*E,'exercise transformed dy coefficient')
zero(curvature(B2,[x,y],0,1)-H-2*x*E,'exercise full curvature')
zero(B2[1].diff(x)-B2[0].diff(y)-H-4*x*E,'exercise derivative alone differs')

# A noncompact nonabelian structure group: affine matrices h(u,v).
affH=s.diag(1,0)
h=s.Matrix([[s.exp(u),v],[0,1]])
c=[x,y,u,v]
base=[y*E,x*affH,s.zeros(2),s.zeros(2)]
omega=[s.simplify(h.inv()*a*h+h.inv()*h.diff(t)) for a,t in zip(base,c)]
fundH=s.Matrix([0,0,1,0]);fundE=s.Matrix([0,0,0,s.exp(u)])
for field,xi in [(fundH,affH),(fundE,E)]:
    zero(sum((omega[i]*field[i] for i in range(4)),s.zeros(2))-xi,
         f'principal vertical reproduction {xi[0,0]}')
zero(fundE.jacobian(c)*fundH-fundH.jacobian(c)*fundE-fundE,
     'right-action fundamental fields have homomorphism sign')
baseF=curvature(base,c,0,1)
for i in range(4):
    for j in range(i+1,4):
        expected=h.inv()*baseF*h if (i,j)==(0,1) else s.zeros(2)
        zero(curvature(omega,c,i,j)-expected,f'principal total-space curvature {i}{j}')
HX=s.Matrix([1,0,0,-y]);HY=s.Matrix([0,1,-x,-x*v])
for name,field in [('x',HX),('y',HY)]:
    zero(sum((omega[i]*field[i] for i in range(4)),s.zeros(2)),f'horizontal lift {name}')
vertical=HY.jacobian(c)*HX-HX.jacobian(c)*HY
curv_at_h=s.simplify(h.inv()*baseF*h)
fund_curv=curv_at_h[0,0]*fundH+curv_at_h[0,1]*fundE
zero(vertical+fund_curv,'horizontal bracket is negative curvature generator')

# Hopf connection pulled back by z = exp(i psi) (1,w)/sqrt(1+|w|^2).
R=1+x*x+y*y
zz=s.exp(s.I*psi)*s.Matrix([1,x+s.I*y])/s.sqrt(R)
oq=[x,y,psi]
hopf=[s.simplify((s.conjugate(zz).T*zz.diff(t))[0]) for t in oq]
for a,b,name in zip(hopf,[-s.I*y/R,s.I*x/R,s.I],['dx','dy','dpsi']):
    zero(a-b,f'Hopf normalized-section connection {name}')
Fxy=s.simplify(hopf[1].diff(x)-hopf[0].diff(y))
zero(Fxy-2*s.I/R**2,'Hopf curvature from differentiated normalized vector')
rr=x*x+y*y
zeta=s.Matrix([x/rr,-y/rr])
A1z=s.Matrix([-s.I*zeta[1],s.I*zeta[0]])/(1+zeta.dot(zeta))
A1w=s.simplify(zeta.jacobian([x,y]).T*A1z)
dphi=s.Matrix([-y/rr,x/rr])
zero(A1w-s.Matrix(hopf[:2])+s.I*dphi,'Hopf overlap potentials and negative winding')
transition=(x-s.I*y)/s.sqrt(rr)
zero(s.Matrix([s.diff(transition,t)/transition for t in [x,y]])+s.I*dphi,
     'Hopf transition Maurer-Cartan form')
Q=s.Matrix([2*x/R,2*y/R,(1-x*x-y*y)/R])
J=Q.jacobian([x,y])
zero(Q.dot(Q)-1,'Hopf base sphere norm')
zero(J.T*J-4*s.eye(2)/R**2,'Hopf base spherical metric')
zero(J[:,0].cross(J[:,1]).dot(Q)-4/R**2,'Hopf chart outward orientation and area')
zero(Fxy-s.I*(J[:,0].cross(J[:,1]).dot(Q))/2,'Hopf curvature area sign')
hx=s.Matrix([1,0,y/R]);hy=s.Matrix([0,1,-x/R])
zero(hy.jacobian(oq)*hx-hx.jacobian(oq)*hy+s.Matrix([0,0,2/R**2]),
     'Hopf horizontal bracket sign')
r=s.symbols('r', positive=True)
zero(s.integrate(2*r/(1+r*r)**2,(r,0,s.oo))-1,'Hopf normalized curvature period')
chi0=-2*s.pi*r*r/(1+r*r)
chi1=2*s.pi/(1+r*r)
zero(chi1-chi0-2*s.pi,'Hopf two chart phase increments')
zero(s.exp(s.I*s.simplify(chi1-chi0))-1,'Hopf phase group elements agree')
k=s.symbols('k',integer=True)
zero(s.I/(2*s.pi)*(2*s.pi*s.I*k)+k,'unitary Chern normalization sign in weight k model')
print(f'PASS: {len(checks)} exact principal-bundle model identities; not an independent review.')
