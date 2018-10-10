import matplotlib.pyplot as plt
from .casteljau import casteljau_points
from .bernstein import intermediate_bern


# Subdivide a curve into two with the same degree of the original one
def subdivide_control_points(method, *points):
    p = method(*points)
    b_left = tuple([p(0, n)(0.5)
                    for n in range(0, len(points))])
    b_right = tuple([p(n, len(points) - 1 - n)(0.5)
                     for n in range(0, len(points))])
    return b_left, b_right


# Calculate the area of the rectangle containing all the points
def rect_area(*points):
    inf = float('inf')
    x_max, y_max, x_min, y_min, = -inf, -inf, inf, inf
    for (x, y) in points:
        x_max, x_min = max(x, x_max), min(x, x_min)
        y_max, y_min = max(y, y_max), min(y, y_min)
    return (x_max - x_min) * (y_max - y_min)


def draw_bezier(method, *points, epsilon=0.0001):
    def _draw_bezier(*_points):
        if rect_area(*_points) / max_area <= epsilon:
            plt.plot(
                [x for (x, y) in _points], [y for (x, y) in _points]
            )
        else:
            b_left, b_right = subdivide_control_points(method, *_points)
            _draw_bezier(*b_left)
            _draw_bezier(*b_right)

    max_area = rect_area(*points)
    _draw_bezier(*points)
    plt.show()


# Draw the curve via Casteljau
def casteljau_draw_bezier(*points, epsilon=0.0001):
    draw_bezier(casteljau_points, *points, epsilon=epsilon)


# Draw the curve via Bernstein
def bernstein_draw_bezier(*points, epsilon=0.0001):
    draw_bezier(intermediate_bern, *points, epsilon=epsilon)
