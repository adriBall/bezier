from .math_utils import transpose, diagonal_transpose, zip_longest


def _not_none(e):
    return e is not None


def _draw_lines(pts, ax, color):
    for row in pts:
        x, y, z = zip_longest(*filter(_not_none, row))
        ax.plot(x, y, z, color=color)


def draw_mesh(pts, ax, color):
    _draw_lines(pts, ax, color)
    _draw_lines(zip_longest(*pts), ax, color)


def draw_tri_mesh(pts, ax, color):
    _draw_lines(pts, ax, color)
    _draw_lines(transpose(pts), ax, color)
    _draw_lines(diagonal_transpose(pts), ax, color)


def draw_points(pts, ax, color):
    for row in pts:
        x, y, z = zip_longest(*row)
        ax.scatter(x, y, z, c=color, s=50)
