from .util import sum_tuple as st, scalar_tuple_product as stp


# Casteljau algorithm
def casteljau_points(*points):
    def P(i, r):
        if (i, r) not in mem:
            if r == 0:
                mem[(i, r)] = lambda t: points[i]
            else:
                mem[(i, r)] = lambda t: st(
                    stp((1 - t), P(i, r - 1)(t)),
                    stp(t, P(i + 1, r - 1)(t))
                )
        return mem[(i, r)]

    mem = {}
    return lambda i, r: mem.get((i, r), P(i, r))


# Parametric curve via Casteljau
def casteljau_bezier_curve(*points):
    p = casteljau_points(*points)
    return lambda t: p(0, len(points) - 1)(t)
