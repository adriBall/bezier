from .util import binomial_coefficient, factorial, sum_tuple as st, scalar_tuple_product as stp


# Bernstein Polynomial
def bern(i, n):
    coef = binomial_coefficient(n, i)
    return lambda t: coef * ((1 - t) ** (n - i)) * (t ** i)


# Barycentric Bernstein polynomial
def bern_bari(i, j, n):
    k = n - i - j
    coef = factorial(n) / (factorial(i) * factorial(j) * factorial(k))
    return lambda u, v: \
        coef * (u ** i) * (v ** j) * ((1 - u - v) ** k)


# Intermediate points of Casteljau algorithm via Bernstein
def intermediate_bern(*points):
    def _p(i, r):
        return lambda t: st(*[stp(bern(j, r)(t), points[i + j])
                              for j in range(r + 1)])

    return lambda i, r: _p(i, r)


# Parametric curve via Bernstein
def bernstein_bezier_curve(*points):
    return lambda t: intermediate_bern(*points)(0, len(points) - 1)(t)


# Parametric surface via Bernstein
def bernstein_bezier_surface(*points):
    m, n = len(points) - 1, len(points[0]) - 1
    bernis = dict({((i, m), bern(i, m)) for i in range(m + 1)})
    bernjs = dict({((j, n), bern(j, n)) for j in range(n + 1)})

    return lambda u, v: st(
        *[stp(bernis[(i, m)](u) * bernjs[(j, n)](v), points[i][j])
          for i in range(m + 1) for j in range(n + 1)])


# Triangular parametric surface via Bernstein
def bernstein_bezier_tri_surface(*points):
    n = len(points) - 1
    berns = dict({((i, j), bern_bari(i, j, n))
                  for i in range(n + 1) for j in range(n + 1 - i)})

    return lambda u, v: st(
        *[stp(berns[(i, j)](u, v), points[i][j])
          for i in range(n + 1) for j in range(n + 1 - i)])
