"""Exact checks for Chapter 15 models; requires SymPy, not a proof checker.

Coordinates, matrix commutators and the Koszul formula provide independent
calculations for the sign-sensitive examples in the text.
"""
import sympy as s

checks = []


def zero(value, name):
    entries = list(value) if isinstance(value, s.MatrixBase) else [value]
    assert all(s.simplify(s.trigsimp(x)) == 0 for x in entries), name
    checks.append(name)


def comm(a, b):
    return a*b-b*a


a, b, t, x, y = s.symbols('a b t x y', real=True)
coords = s.Matrix([a, b])
HL, EL = s.Matrix([a, 0]), s.Matrix([0, a])
HR, ER = s.Matrix([a, b]), s.Matrix([0, 1])
zero(EL.jacobian(coords)*HL-HL.jacobian(coords)*EL-EL, 'affine left bracket')
zero(ER.jacobian(coords)*HR-HR.jacobian(coords)*ER+ER, 'affine right anti-bracket')
theta = s.diag(1/a, 1/a)
zero(theta*s.Matrix.hstack(HL, EL)-s.eye(2), 'affine Maurer-Cartan duality')
zero(s.diff(1/a, a)+1/a**2, 'affine d theta_E sign')
curve = s.Matrix([s.exp(t*x), y*(s.exp(t*x)-1)/x])
zero(curve.diff(t)-s.Matrix([x*curve[0], y*curve[0]]), 'affine exponential ODE')
zero(s.limit(curve[1], x, 0)-t*y, 'affine exponential removable singularity')
affH, affE = s.diag(0, 1), s.Matrix([[0, 0], [-1, 0]])
zero(s.Matrix(2, 2, lambda i,j:s.trace([affH,affE][i]*[affH,affE][j]))
     -s.diag(1,0), 'affine Killing degeneracy')

H = s.diag(1, -1)
E = s.Matrix([[0,1],[0,0]])
F = E.T
basis = [H,E,F]


def slcoords(M):
    return s.Matrix([M[0,0], M[0,1], M[1,0]])


ad = [s.Matrix.hstack(*(slcoords(comm(X,Y)) for Y in basis)) for X in basis]
for i,X in enumerate(basis):
    for j,Y in enumerate(basis):
        zero(s.trace(ad[i]*ad[j])-4*s.trace(X*Y), f'sl2 Killing {i}{j}')
g = s.diag(s.exp(t), s.exp(-t))
for i,Y in enumerate(basis):
    zero(slcoords(g*Y*g.inv())-(t*ad[0]).exp()[:,i], f'sl2 Ad exp {i}')
negative = s.diag(-2,-s.Rational(1,2))
z11,z12,z21,z22=s.symbols('z11 z12 z21 z22')
Z=s.Matrix([[z11,z12],[z21,z22]])
zero(comm(Z,negative)-s.Matrix([[0,s.Rational(3,2)*z12],
                              [-s.Rational(3,2)*z21,0]]), 'distinct eigenvalue centralizer')
rot=s.Matrix([[s.cos(s.pi*t),-s.sin(s.pi*t)],
              [s.sin(s.pi*t),s.cos(s.pi*t)]])
path=rot*s.diag(2**t,2**(-t))
zero(path.det()-1, 'non-exponential element path determinant')
zero(path.subs(t,1)-negative, 'non-exponential element path endpoint')


def hat(v):
    return s.Matrix([[0,-v[2],v[1]],[v[2],0,-v[0]],[-v[1],v[0],0]])


vectors=[s.eye(3)[:,i] for i in range(3)]
so=[hat(v) for v in vectors]
for i,v in enumerate(vectors):
    for j,w in enumerate(vectors):
        zero(comm(so[i],so[j])-hat(v.cross(w)), f'so3 commutator {i}{j}')
        zero(s.trace(so[i]*so[j])+2*v.dot(w), f'so3 Killing {i}{j}')
v=s.Matrix([1,2,2]);A=hat(v)
Q=s.eye(3)+s.sin(3*t)*A/3+(1-s.cos(3*t))*A*A/9
zero(Q.diff(t)-Q*A, 'Rodrigues ODE non-coordinate axis')
zero(Q.T*Q-s.eye(3), 'Rodrigues orthogonality')
zero(Q.det()-1, 'Rodrigues orientation')

# Koszul coefficients for a general diagonal left-invariant metric.
I1,I2,I3=s.symbols('I1 I2 I3', positive=True)
metric=s.diag(I1,I2,I3)


def bracket(u,v):
    return u.cross(v)


def connection(u,v,met):
    cov=s.Matrix([((bracket(u,v).T*met*w)[0]
                   -(bracket(v,w).T*met*u)[0]
                   +(bracket(w,u).T*met*v)[0])/2 for w in vectors])
    return met.inv()*cov


for i,u in enumerate(vectors):
    for j,v in enumerate(vectors):
        zero(connection(u,v,s.eye(3))-bracket(u,v)/2, f'Koszul bi-invariant {i}{j}')
        for k,w in enumerate(vectors):
            R=connection(u,connection(v,w,s.eye(3)),s.eye(3))\
              -connection(v,connection(u,w,s.eye(3)),s.eye(3))\
              -connection(bracket(u,v),w,s.eye(3))
            zero(R+bracket(bracket(u,v),w)/4, f'curvature sign {i}{j}{k}')
zero(connection(vectors[0]+vectors[1],vectors[0]+vectors[1],metric)
     -s.Matrix([0,0,(I2-I1)/I3]), 'anisotropic group exponential acceleration')

# Ambient orthogonal reflection, checked with an exact non-axis unit vector.
p=s.Matrix([1,2,2])/3
reflection=2*p*p.T-s.eye(3)
zero(reflection.T*reflection-s.eye(3), 'sphere symmetry orthogonal')
zero(reflection*p-p, 'sphere symmetry fixes p')
for w in [s.Matrix([2,-1,0]),s.Matrix([2,0,-1])]:
    zero(reflection*w+w, 'sphere symmetry tangent minus identity')
print(f'PASS: {len(checks)} exact model identities; not an independent mathematical review.')
