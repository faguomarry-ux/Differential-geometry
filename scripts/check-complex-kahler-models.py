"""Exact coordinate checks for Chapter 17, not a general proof or independent review.

Requires SymPy. Conjugate coordinates are independent symbols for Wirtinger
derivatives; the real two-dimensional metric is also checked independently.
"""
import sympy as s

checks = []


def zero(value, name):
    entries = list(value) if isinstance(value, s.MatrixBase) else [value]
    assert all(s.simplify(v) == 0 for v in entries), name
    checks.append(name)


z1, z2, b1, b2 = s.symbols('z1 z2 b1 b2')
z = [z1, z2]
b = [b1, b2]
q = 1 + z1*b1 + z2*b2
potential = s.log(q)
G = s.Matrix(2, 2, lambda i, j: s.diff(potential, z[i], b[j]))
expected = s.eye(2)/q-s.Matrix(b)*s.Matrix([z])/q**2
zero(G-expected, 'FS Hessian from potential')
zero(G.det()-q**-3, 'FS determinant in complex dimension two')
for i in range(2):
    for j in range(2):
        for k in range(2):
            zero(G[j, k].diff(z[i])-G[i, k].diff(z[j]), f'FS closure {i}{j}{k}')
for i in range(2):
    for j in range(2):
        zero(-s.diff(s.log(G.det()), z[i], b[j])-3*G[i, j], f'FS Ricci {i}{j}')

# A non-diagonal, nonconstant positive Hermitian bundle metric.
H = s.Matrix([[1+z1*b1, z2], [b2, 1+z2*b2]])
zero(H.det()-(1+z1*b1*(1+z2*b2)), 'positive determinant model')
A = [s.simplify(H.inv()*H.diff(t)) for t in z]
F = {(i, j): -A[i].diff(b[j]) for i in range(2) for j in range(2)}
zero(A[1].diff(z1)-A[0].diff(z2)+A[0]*A[1]-A[1]*A[0], 'Chern (2,0) cancellation')
for i in range(2):
    zero(H*A[i]-H.diff(z[i]), f'metric (1,0) compatibility {i}')
    for j in range(2):
        zero(s.trace(F[i, j])+s.diff(s.log(H.det()), z[i], b[j]), f'trace curvature {i}{j}')

# Holomorphic change of frame, using conjugate variables in G*.
frame = s.Matrix([[1, z1], [0, 1]])
frame_star = s.Matrix([[1, 0], [b1, 1]])
Hp = frame_star*H*frame
Ap = [s.simplify(Hp.inv()*Hp.diff(t)) for t in z]
for i in range(2):
    zero(Ap[i]-frame.inv()*A[i]*frame-frame.inv()*frame.diff(z[i]), f'Chern gauge potential {i}')
    for j in range(2):
        zero(-Ap[i].diff(b[j])-frame.inv()*F[i, j]*frame, f'Chern curvature covariance {i}{j}')

# Compute all real Christoffels and Riemann components of CP1 directly.
x, y = s.symbols('x y', real=True)
coords = [x, y]
g = 2*s.eye(2)/(1+x*x+y*y)**2
ginv = g.inv()
Gamma = [[[s.simplify(sum(ginv[k, l]*(s.diff(g[l, j], coords[i])+s.diff(g[l, i], coords[j])-s.diff(g[i, j], coords[l])) for l in range(2))/2) for j in range(2)] for i in range(2)] for k in range(2)]
R = {}
for k in range(2):
    for l in range(2):
        for i in range(2):
            for j in range(2):
                R[k, l, i, j] = s.simplify(s.diff(Gamma[k][j][l], coords[i])-s.diff(Gamma[k][i][l], coords[j])+sum(Gamma[k][i][a]*Gamma[a][j][l]-Gamma[k][j][a]*Gamma[a][i][l] for a in range(2)))
                constant_curvature = 2*((1 if k == i else 0)*g[j, l]-(1 if k == j else 0)*g[i, l])
                zero(R[k, l, i, j]-constant_curvature, f'CP1 real curvature {k}{l}{i}{j}')
Ric = s.Matrix(2, 2, lambda i, j: sum(R[a, j, a, i] for a in range(2)))
zero(Ric-2*g, 'CP1 real Ricci and scale')

# Tautological holomorphic and unitary frames, converted to real coordinates.
Q = 1+z1*b1
Ahol = b1/Q
zero(-s.diff(Ahol, b1)+Q**-2, 'tautological Chern curvature')
unit_z = Ahol-s.diff(s.log(Q), z1)/2
unit_b = -s.diff(s.log(Q), b1)/2
real_sub = {z1: x+s.I*y, b1: x-s.I*y}
zero((unit_z+unit_b).subs(real_sub)+s.I*y/(1+x*x+y*y), 'unitary Hopf dx potential')
zero((s.I*unit_z-s.I*unit_b).subs(real_sub)-s.I*x/(1+x*x+y*y), 'unitary Hopf dy potential')
r = s.symbols('r', positive=True)
zero(s.integrate(4*s.pi*r/(1+r*r)**2, (r, 0, s.oo))-2*s.pi, 'FS area integral')
zero(-s.integrate(2*r/(1+r*r)**2, (r, 0, s.oo))+1, 'tautological iF/2pi period')

# Nonintegrable eigendistributions: full variable-coefficient brackets.
variables = [z1, z2, b1, b2]
Z1 = s.Matrix([1, 0, 0, 0])
Z2 = s.Matrix([0, 1, z1, 0])
W1 = s.Matrix([0, 0, 1, 0])
W2 = s.Matrix([b1, 0, 0, 1])
basis = s.Matrix.hstack(Z1, Z2, W1, W2)
J = basis*s.diag(s.I, s.I, -s.I, -s.I)*basis.inv()


def bracket(U, V):
    return s.Matrix([sum(U[a]*s.diff(V[k], variables[a])-V[a]*s.diff(U[k], variables[a]) for a in range(4)) for k in range(4)])


zero(basis.det()-1, 'eigenframes complementary everywhere')
zero(J*J+s.eye(4), 'almost complex tensor squares to minus identity')
zero(bracket(W1, W2)-Z1, 'nonintegrable bracket')
N = bracket(J*W1, J*W2)-J*bracket(J*W1, W2)-J*bracket(W1, J*W2)-bracket(W1, W2)
zero(N+4*Z1, 'Nijenhuis coefficient minus four')
f = z1
projected_second = sum(W1[a]*s.diff(sum(W2[k]*s.diff(f, variables[k]) for k in range(4)), variables[a]) for a in range(4))-sum(W2[a]*s.diff(sum(W1[k]*s.diff(f, variables[k]) for k in range(4)), variables[a]) for a in range(4))
zero(projected_second-1, 'bar-partial square on z1 in eigenframe')

C = s.Matrix([[1+s.I, 2-s.I], [s.I, 3+2*s.I]])
real_C = s.BlockMatrix([[s.re(C), -s.im(C)], [s.im(C), s.re(C)]]).as_explicit()
zero(real_C.det()-C.det()*s.conjugate(C.det()), 'real determinant is complex modulus square')
for m in range(1, 5):
    zero(s.diag(*([1, -1]*m)).det()-(-1)**m, f'conjugation orientation dimension {m}')

print(f'PASS: {len(checks)} exact complex/Kahler model identities; not an independent review.')
