"""Exact coordinate and exterior-algebra models for Chapter 18.

Requires SymPy. These finite examples are not a proof checker or an independent
mathematical review. Matrix coefficients preserve their noncommuting order.
"""
from itertools import permutations
from math import factorial
import sympy as s

checks = []
x, y, z, w, v, t, u = s.symbols('x y z w v t u', real=True)
coordinates = [x, y, z, w, v]


def zero(value, name):
    entries = list(value) if isinstance(value, s.MatrixBase) else [value]
    assert all(s.simplify(entry) == 0 for entry in entries), name
    checks.append(name)


class Form:
    def __init__(self, size, values=None):
        self.size = size
        self.values = {} if values is None else values

    def __add__(self, other):
        assert self.size == other.size
        keys = self.values.keys() | other.values.keys()
        return Form(self.size, {key: self.values.get(key, s.zeros(self.size))+other.values.get(key, s.zeros(self.size)) for key in keys})

    def scale(self, coefficient):
        return Form(self.size, {key: matrix*coefficient for key, matrix in self.values.items()})

    def __sub__(self, other):
        return self+other.scale(-1)

    def wedge(self, other):
        assert self.size == other.size
        out = {}
        for left, A in self.values.items():
            for right, B in other.values.items():
                if set(left) & set(right):
                    continue
                key = tuple(sorted(left+right))
                sign = (-1)**sum(i > j for i in left for j in right)
                out[key] = out.get(key, s.zeros(self.size))+sign*A*B
        return Form(self.size, out)

    def d(self):
        out = {}
        for key, A in self.values.items():
            for i, coordinate in enumerate(coordinates):
                if i in key:
                    continue
                target = tuple(sorted((i,)+key))
                sign = (-1)**sum(j < i for j in key)
                out[target] = out.get(target, s.zeros(self.size))+sign*A.diff(coordinate)
        return Form(self.size, out)

    def trace(self):
        return Form(1, {key: s.Matrix([[s.trace(A)]]) for key, A in self.values.items()})

    def diff(self, parameter):
        return Form(self.size, {key: A.diff(parameter) for key, A in self.values.items()})

    def integral(self, parameter):
        return Form(self.size, {key: A.applyfunc(lambda c: s.integrate(s.expand(c), (parameter, 0, 1))) for key, A in self.values.items()})

    def substitute(self, mapping):
        return Form(self.size, {key: A.subs(mapping) for key, A in self.values.items()})

    def conjugate_by(self, matrix):
        inverse = matrix.inv()
        return Form(self.size, {key: inverse*A*matrix for key, A in self.values.items()})


def check_form(form, name):
    for key, value in sorted(form.values.items()):
        zero(value, name+' '+str(key))


H = s.diag(1, -1)
E = s.Matrix([[0, 1], [0, 0]])
N = E.T
A0 = Form(2, {(0,): y*E, (1,): z*H, (2,): w*N, (3,): v*E, (4,): x*N})
A1 = Form(2, {(0,): w*H, (1,): x*E, (2,): y*N, (3,): z*(H+E), (4,): v*N})


def curvature(A):
    return A.d()+A.wedge(A)


F0, F1 = curvature(A0), curvature(A1)
check_form(F1.d()+A1.wedge(F1)-F1.wedge(A1), 'Bianchi on five-dimensional model')
check_form(F1.trace().d(), 'closed trace of curvature')
check_form(F1.wedge(F1).trace().d(), 'closed trace square in dimension five')
check_form(A1.wedge(A1).wedge(A1).wedge(A1).trace(), 'odd cyclic trace kills A4')

a = A1-A0
At = A0+a.scale(t)
Ft = curvature(At)
check_form(Ft.diff(t)-(a.d()+At.wedge(a)+a.wedge(At)), 'curvature path derivative')
T = a.wedge(Ft).trace().scale(2).integral(t)
check_form(T.d()-(F1.wedge(F1).trace()-F0.wedge(F0).trace()), 'relative transgression coefficient and sign')

CS = (A1.wedge(A1.d())+A1.wedge(A1).wedge(A1).scale(s.Rational(2, 3))).trace()
check_form(CS.d()-F1.wedge(F1).trace(), 'local CS3 differential')

# Fixed-endpoint path homotopy; its correction has the sign in the text.
C = Form(2, {(0,): E, (1,): N, (4,): H})
Ast = At+C.scale(u*t*(1-t))
ap, bp = Ast.diff(t), Ast.diff(u)
correction = ap.wedge(bp).trace().scale(-2).integral(t).integral(u)
Tcurved = ap.wedge(curvature(Ast)).trace().scale(2).substitute({u: 1}).integral(t)
check_form(Tcurved-T-correction.d(), 'fixed-endpoint homotopy correction')

# Polynomial noncommutative gauge transformation.
g = s.eye(2)+x*E
gauge = Form(2, {(i,): g.inv()*g.diff(coordinate) for i, coordinate in enumerate(coordinates)})
Ag = A1.conjugate_by(g)+gauge
Fg = curvature(Ag)
check_form(Fg-F1.conjugate_by(g), 'gauge curvature covariance')
check_form(Fg.wedge(Fg).trace()-F1.wedge(F1).trace(), 'invariant trace polynomial')

# A concrete check of the graded sign in Freed Exercise 6.1.13.
alpha = Form(2, {(0,): E})
beta = Form(2, {(1,): N})
graded = alpha.wedge(beta)+beta.wedge(alpha)
check_form(graded.trace(), 'graded commutator trace')
ordinary = (alpha.wedge(beta)-beta.wedge(alpha)).trace()
zero(ordinary.values[(0, 1)][0]-2, 'ordinary commutator is not trace-free for odd forms')

# Pfaffian, realification, and normalization identities on the Lie algebra.
a1, a2, a3, a4, a5, a6 = s.symbols('a1:7', real=True)
X = s.Matrix([[0, a1, a2, a3], [-a1, 0, a4, a5], [-a2, -a4, 0, a6], [-a3, -a5, -a6, 0]])


def pf4(matrix):
    return matrix[0, 1]*matrix[2, 3]-matrix[0, 2]*matrix[1, 3]+matrix[0, 3]*matrix[1, 2]


zero(pf4(X)**2-X.det(), 'Pfaffian squared is determinant')
swap = s.eye(4)
swap.row_swap(0, 1)
zero(pf4(swap.T*X*swap)+pf4(X), 'orientation reversal of Pfaffian')
parameter = s.symbols('parameter')
zero((s.eye(4)+parameter*X).det().coeff(parameter, 2)+s.trace(X*X)/2, 'first Pontryagin coefficient')
aa, bb, cc, dd = s.symbols('aa bb cc dd', real=True)
U = s.Matrix([[s.I*aa, bb+s.I*cc], [-bb+s.I*cc, s.I*dd]])
real_U = s.BlockMatrix([[s.re(U), -s.im(U)], [s.im(U), s.re(U)]]).as_explicit()
real_U = real_U.extract([0, 2, 1, 3], [0, 2, 1, 3])
zero(pf4(real_U)-(s.I*U).det(), 'Euler equals top Chern in complex orientation')
c1 = s.trace(s.I*U)/(2*s.pi)
c2 = (s.I*U).det()/(4*s.pi**2)
zero(-s.trace(real_U*real_U)/(8*s.pi**2)-(c1*c1-2*c2), 'p1 of underlying real complex bundle')

pauli = [s.Matrix([[0, 1], [1, 0]]), s.Matrix([[0, -s.I], [s.I, 0]]), s.diag(1, -1)]
Tsu = [(-s.I/2)*matrix for matrix in pauli]
for i in range(3):
    for j in range(3):
        zero(Tsu[i]*Tsu[j]-Tsu[j]*Tsu[i]-sum((s.LeviCivita(i, j, k)*Tsu[k] for k in range(3)), s.zeros(2)), f'SU2 bracket {i}{j}')
        for k in range(3):
            zero(s.trace(Tsu[i]*Tsu[j]*Tsu[k])+s.LeviCivita(i, j, k)/4, f'SU2 cubic trace {i}{j}{k}')
cubic = sum(s.LeviCivita(*order)*s.trace(Tsu[order[0]]*Tsu[order[1]]*Tsu[order[2]]) for order in permutations(range(3)))
zero(-cubic/3-s.Rational(1, 2), 'pure-gauge CS3 is nonzero volume form')

# Independent exact radial integrals fix the sphere and projective scales.
radial = s.symbols('radial', positive=True)
for r in range(1, 6):
    pf_coefficient = s.factorial(2*r)/((2*s.pi)**r*2**r*s.factorial(r))
    sphere_area = 2*s.pi**(r+s.Rational(1, 2))/s.gamma(r+s.Rational(1, 2))
    zero(pf_coefficient*sphere_area-2, f'round sphere Euler integral dimension {2*r}')
for m in range(1, 5):
    beta_integral = s.integrate(radial**(2*m-1)/(1+radial**2)**(m+1), (radial, 0, s.oo))
    zero(beta_integral-s.Rational(1, 2*m), f'projective radial integral {m}')
    volume = s.factorial(m)/s.pi**m*2*s.pi**m/s.factorial(m-1)*beta_integral
    zero(volume-1, f'projective normalized top power {m}')

ra, rb = s.symbols('ra rb')
zero((ra+rb)**2-2*ra*rb-(ra**2+rb**2), 'line-sum p1 and Chern character')
zero(3**2-2*3-3, 'CP2 Pontryagin number')
zero(8-2*4, 'product surface Pontryagin number')
print(f'PASS: {len(checks)} exact characteristic-class model identities; not an independent review.')
