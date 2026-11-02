"""Exact finite models for Chapter 19; not a proof checker or independent review.

Optional dependency: SymPy. The normal book build does not call this script.
"""
from itertools import product
import sympy as s

checks = 0


def check(expression, expected=0):
    global checks
    delta = expression - expected
    entries = list(delta) if isinstance(delta, s.MatrixBase) else [delta]
    assert all(s.simplify(s.expand_trig(x)) == 0 for x in entries), delta
    checks += 1


def fock(m):
    dim = 2**m
    creators = []
    for j in range(m):
        matrix = s.zeros(dim)
        for mask in range(dim):
            if not mask & (1 << j):
                sign = (-1)**((mask & ((1 << j)-1)).bit_count())
                matrix[mask | (1 << j), mask] = sign
        creators.append(matrix)
    gamma = []
    for a in creators:
        gamma += [a-a.T, s.I*(a+a.T)]
    return creators, gamma


for m in (1, 2, 3):
    creators, c = fock(m)
    identity = s.eye(2**m)
    for j, k in product(range(2*m), repeat=2):
        check(c[j]*c[k]+c[k]*c[j], -2*identity if j == k else s.zeros(2**m))
    for matrix in c:
        check(matrix.conjugate().T, -matrix)
    chirality = s.I**m * s.prod(c)
    parity = s.diag(*[(-1)**mask.bit_count() for mask in range(2**m)])
    check(chirality, parity)
    check(chirality**2, identity)
    check(chirality.conjugate().T, chirality)
    for matrix in c:
        check(chirality*matrix+matrix*chirality, s.zeros(2**m))
    for odd_sign in (-1, 1):
        odd = odd_sign*s.I*chirality
        check(odd**2, -identity)
        check(-s.I*chirality*odd, odd_sign*identity)
    # Matrix-unit argument: the vacuum projector has exactly rank one.
    projector = s.eye(2**m)
    for a in creators:
        projector *= identity-a*a.T
    check(projector, s.diag(1, *([0]*(2**m-1))))
    assert projector.rank() == 1

_, c = fock(2)
identity = s.eye(4)
for i in range(4):
    for j in range(i+1, 4):
        for k in range(4):
            expected = (c[j] if k == i else s.zeros(4)) - (c[i] if k == j else s.zeros(4))
            check((c[i]*c[j]*c[k]-c[k]*c[i]*c[j])/2, expected)

theta = s.symbols('theta', real=True)
lift = s.cos(theta/2)*identity+s.sin(theta/2)*c[0]*c[1]
inverse = lift.conjugate().T
check(lift*inverse, identity)
check(lift*c[0]*inverse, s.cos(theta)*c[0]+s.sin(theta)*c[1])
check(lift*c[1]*inverse, -s.sin(theta)*c[0]+s.cos(theta)*c[1])
check(lift.subs(theta, 2*s.pi), -identity)
check(lift.subs(theta, 4*s.pi), identity)

# Two independent second fundamental forms produce a nonconstant algebraic
# curvature model. Contract all 256 terms, retaining Clifford multiplication.
a, b, d = s.symbols('a b d', real=True)
forms = [s.Matrix([[a, 1, 2, 0], [1, b, 0, 3], [2, 0, d, 1], [0, 3, 1, 2]]),
         s.Matrix([[1, 2, 0, b], [2, a, 1, 0], [0, 1, 3, d], [b, 0, d, 1]])]


def curvature(i, j, k, l):
    return sum(h[j, k]*h[i, l]-h[i, k]*h[j, l] for h in forms)


contraction = s.zeros(4)
for i, j, k, l in product(range(4), repeat=4):
    contraction += curvature(i, j, k, l)*c[i]*c[j]*c[k]*c[l]/8
scalar = sum(curvature(i, j, j, i) for i, j in product(range(4), repeat=2))
check(contraction, scalar*identity/4)
for i, j, k, l in [(0, 1, 2, 3), (0, 2, 1, 3), (1, 2, 3, 0)]:
    check(curvature(i, j, k, l)-curvature(i, k, j, l)+curvature(i, l, j, k))

_, two = fock(1)
c1, c2 = two
grading = s.I*c1*c2
x, y, B = s.symbols('x y B', real=True)
psi = s.Matrix([x**3+x*y+s.I*y**2, x**2*y+s.I*x+y**3])


def magnetic_dirac(v):
    return c1*v.diff(x)+c2*(v.diff(y)+s.I*B*x*v)


rough = -psi.diff(x, 2)-((psi.diff(y)+s.I*B*x*psi).diff(y)+s.I*B*x*(psi.diff(y)+s.I*B*x*psi))
check(magnetic_dirac(magnetic_dirac(psi)), rough+B*grading*psi)

# Independent local differential-operator calculation on the round S2:
# e1=partial_x, e2=csc(x) partial_y. This tests the lifted connection factor
# as well as the scalar-curvature correction, rather than only gamma algebra.
def sphere_nabla2(v):
    return v.diff(y)/s.sin(x)+s.cot(x)*c1*c2*v/2


def sphere_dirac(v):
    return c1*v.diff(x)+c2*sphere_nabla2(v)


sphere_rough = -psi.diff(x, 2)-sphere_nabla2(sphere_nabla2(psi))-s.cot(x)*psi.diff(x)
check(sphere_dirac(sphere_dirac(psi)), sphere_rough+psi/2)

# All four torus signs, explicit pullback of characters under the two
# modular generators. Zero is fixed; the three other characters form an orbit.
S = s.Matrix([[0, -1], [1, 0]])
T = s.Matrix([[1, 1], [0, 1]])
for sign in product((0, 1), repeat=2):
    for matrix in (S, T):
        out = matrix.T*s.Matrix(sign)
        for loop in [(1, 0), (0, 1), (1, 1)]:
            check(s.Integer(-1)**int((s.Matrix(sign).T*matrix*s.Matrix(loop))[0]),
                  s.Integer(-1)**int((out.T*s.Matrix(loop))[0]))
orbit = {(1, 0)}
while True:
    expanded = orbit | {tuple(int(v) % 2 for v in A.T*s.Matrix(q)) for q in orbit for A in (S, T)}
    if expanded == orbit:
        break
    orbit = expanded
assert orbit == {(1, 0), (0, 1), (1, 1)}
checks += 1

u, v, w = s.symbols('u v w', real=True)
H = s.Matrix([[u, v], [v, w]])
determinant = s.expand((s.eye(2)+s.I*H).det())
check(s.re(determinant), 1-H.det())
check(s.im(determinant), s.trace(H))
check((s.eye(2)+H**2).det(), determinant*s.conjugate(determinant))
check(s.re(determinant).subs(w, -u), 1+u**2+v**2)
check((1+s.I*s.sqrt(3))**3, -8)
H3 = s.Matrix([[u, v, 1], [v, w, 2], [1, 2, a]])
det3 = s.expand((s.eye(3)+s.I*H3).det())
sigma2 = (s.trace(H3)**2-s.trace(H3**2))/2
check(s.im(det3), s.trace(H3)-H3.det())
check(s.re(det3), 1-sigma2)
check((s.eye(3)+H3**2).det(), det3*s.conjugate(det3))

alpha, beta = s.symbols('alpha beta', real=True)
basis = s.zeros(8, 4)
basis[0, 0] = 1
basis[1, 1], basis[2, 1] = s.cos(alpha), s.sin(alpha)
basis[4, 2] = 1
basis[5, 3], basis[6, 3] = s.cos(beta), s.sin(beta)
check(basis.T*basis, s.eye(4))
omega = s.diag(*([s.Matrix([[0, 1], [-1, 0]])]*4))
restricted = basis.T*omega*basis
pfaffian = restricted[0, 1]*restricted[2, 3]-restricted[0, 2]*restricted[1, 3]+restricted[0, 3]*restricted[1, 2]
check(pfaffian, s.cos(alpha)*s.cos(beta))

print(f'PASS: {checks} exact spin/calibration model identities; not an independent review.')
