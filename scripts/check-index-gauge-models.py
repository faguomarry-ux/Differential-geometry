"""Exact Chapter 20 models; not a general proof or independent review.

Optional dependency: SymPy. The normal build does not call this script.
"""
from itertools import combinations
import sympy as s

checks = 0


def check(actual, expected=0):
    global checks
    delta = actual - expected
    entries = list(delta) if isinstance(delta, s.MatrixBase) else [delta]
    if not all(s.simplify(x) == 0 for x in entries):
        raise AssertionError(delta)
    checks += 1


pairs = list(combinations(range(4), 2))


def sign(seq):
    return (-1) ** sum(seq[i] > seq[j] for i in range(len(seq)) for j in range(i+1, len(seq)))


star = s.zeros(6)
for j, pair in enumerate(pairs):
    comp = tuple(i for i in range(4) if i not in pair)
    star[pairs.index(comp), j] = sign(pair+comp)
proj = (s.eye(6)+star)/2
check(star**2, s.eye(6))
check(star.T, star)
check(proj**2, proj)
check(s.trace(proj), 3)

# Arbitrary cotangent vector: symbol exactness and the sqrt(2) normalization.
xi = s.Matrix(s.symbols('x1:5', real=True))
wedge = s.zeros(6, 4)
for k, (i, j) in enumerate(pairs):
    wedge[k, j], wedge[k, i] = xi[i], -xi[j]
symbol_plus = proj*wedge
check(wedge*xi, s.zeros(6, 1))
check(symbol_plus*xi, s.zeros(6, 1))
norm_xi = (xi.T*xi)[0]
check(xi*xi.T + 2*symbol_plus.T*symbol_plus, norm_xi*s.eye(4))
for v in [s.eye(4)[:, j] for j in range(4)] + [s.Matrix([1, 2, -3, 4])]:
    mat = symbol_plus.subs(dict(zip(xi, v)))
    assert mat.rank() == 3
    check(mat*v, s.zeros(6, 1))

# Noncommuting su(2)-valued 2-form: trace wedge and both energy decompositions.
pauli = [s.Matrix([[0, 1], [1, 0]]), s.Matrix([[0, -s.I], [s.I, 0]]), s.diag(1, -1)]
gens = [-s.I*m for m in pauli]
f = [sum(((j+1)*gens[j % 3], gens[(j+1) % 3]), s.zeros(2)) for j in range(6)]
for matrix in f:
    check(matrix.conjugate().T, -matrix)
    check(s.trace(matrix))
fp = [(f[j]+sum((star[j, k]*f[k] for k in range(6)), s.zeros(2)))/2 for j in range(6)]
fm = [f[j]-fp[j] for j in range(6)]
energy = lambda form: -sum(s.trace(m*m) for m in form)
top = sum(sign(p+q)*s.trace(f[j]*f[k])
          for j, p in enumerate(pairs) for k, q in enumerate(pairs) if not set(p)&set(q))
check(top, energy(fm)-energy(fp))
check(energy(f), energy(fp)+energy(fm))
check(energy(f), top+2*energy(fp))
check(energy(f), -top+2*energy(fm))
check(-sum(s.trace(a*b) for a, b in zip(fp, fm)))

# Polynomial connection model, rather than assuming the curvature variation.
x = s.symbols('y0:4', real=True)
t = s.symbols('t', real=True)
A = [x[(j+1) % 4]*gens[j % 3] for j in range(4)]
a = [(x[j]**2+1)*gens[(j+1) % 3] for j in range(4)]
At = [A[j]+t*a[j] for j in range(4)]
curvature = lambda conn, i, j: (conn[j].diff(x[i])-conn[i].diff(x[j])
                                +conn[i]*conn[j]-conn[j]*conn[i])
for i, j in pairs:
    f0, ft = curvature(A, i, j), curvature(At, i, j)
    da = (a[j].diff(x[i])-a[i].diff(x[j])+A[i]*a[j]-a[j]*A[i]
          -A[j]*a[i]+a[i]*A[j])
    check(ft, f0+t*da+t**2*(a[i]*a[j]-a[j]*a[i]))
    check((-s.trace(ft*ft)).diff(t).subs(t, 0), -2*s.trace(f0*da))

# A-hat coefficients through form degree eight.
z, w, eps = s.symbols('z w eps')
q = lambda y: (y/2)/s.sinh(y/2)
expansion = s.series(q(eps*z)*q(eps*w), eps, 0, 6).removeO().expand()
check(expansion.coeff(eps, 2), -(z*z+w*w)/24)
check(expansion.coeff(eps, 4), (7*(z*z+w*w)**2-4*z*z*w*w)/5760)
c1, c2, p1, r = s.symbols('c1 c2 p1 r')
check(s.expand((1-p1*eps**4/24)*(r+c1*eps**2+(c1**2/2-c2)*eps**4)).coeff(eps, 4),
      c1**2/2-c2-r*p1/24)

# Fock representation in dimension four; even basis masks are 0 and 3.
creators = []
for j in range(2):
    m = s.zeros(4)
    for mask in range(4):
        if not mask & (1 << j):
            m[mask | (1 << j), mask] = (-1)**((mask & ((1 << j)-1)).bit_count())
    creators.append(m)
c = []
for m in creators:
    c += [m-m.T, s.I*(m+m.T)]
gamma = -c[0]*c[1]*c[2]*c[3]
check(gamma, s.diag(1, -1, -1, 1))
plus, minus = [0, 3], [1, 2]
cliff = lambda form: sum((form[j]*c[i]*c[k] for j, (i, k) in enumerate(pairs)), s.zeros(4))
images = []
for k in [0, 1, 2]:
    sd = s.eye(6)[:, k]+star*s.eye(6)[:, k]
    asd = s.eye(6)[:, k]-star*s.eye(6)[:, k]
    m = cliff(s.I*sd).extract(plus, plus)
    images.append(m)
    check(m.conjugate().T, m)
    check(s.trace(m))
    check(cliff(s.I*sd).extract(minus, minus), s.zeros(2))
    check(cliff(s.I*asd).extract(plus, plus), s.zeros(2))
assert s.Matrix.hstack(*(m.reshape(4, 1) for m in images)).rank() == 3
u, v, h, k = s.symbols('u v h k', real=True)
psi = s.Matrix([u+s.I*v, h+s.I*k])
norm = (psi.conjugate().T*psi)[0].expand()
Q = psi*psi.conjugate().T - norm*s.eye(2)/2
check(Q.conjugate().T, Q)
check(s.trace(Q))
check(Q*psi, norm*psi/2)
check(s.trace(Q*Q), norm**2/2)
check((psi.conjugate().T*(Q/2)*psi)[0], norm**2/4)

# Spin-c gauge covariance; determinant gauge coefficient must be two.
theta = x[0]*x[1]+x[2]**2
phase = s.exp(s.I*theta)
section = s.Matrix([x[0]+s.I*x[2], x[1]*x[3]])
for j in range(4):
    Bj = s.I*(j+1)*x[j]
    Bnew = Bj-2*s.I*s.diff(theta, x[j])
    check((phase*section).diff(x[j])+Bnew*(phase*section)/2
          -phase*(section.diff(x[j])+Bj*section/2), s.zeros(2, 1))

# Integer-flux torus family, including a nonminimal Yang-Mills critical point.
for a0, b0 in [(1, -1), (1, 1), (1, 0), (2, -3), (0, 0)]:
    curv = s.Matrix([a0, 0, 0, 0, 0, b0])
    plus_norm = 8*s.pi**2*((proj*curv).T*(proj*curv))[0]
    minus_norm = 8*s.pi**2*(((s.eye(6)-proj)*curv).T*((s.eye(6)-proj)*curv))[0]
    chern = -2*a0*b0
    check(minus_norm-plus_norm, 8*s.pi**2*chern)
    check(plus_norm+minus_norm, 8*s.pi**2*(a0*a0+b0*b0))

print(f"OK: {checks} exact index/gauge model identities; not a general proof or independent review.")
