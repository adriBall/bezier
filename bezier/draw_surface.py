import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from .bernstein import bernstein_bezier_surface, bernstein_bezier_tri_surface
from .util import draw_mesh, draw_tri_mesh, draw_points, gridspace


def draw_surface(*points, n=20):
    u, v = gridspace(0, 1, n, d=2)

    surface = bernstein_bezier_surface(*points)
    surface_pts = [[surface(x, y) for y in v] for x in u]

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    draw_mesh(surface_pts, ax, 'b')
    draw_mesh(points, ax, 'r')
    draw_points(points, ax, 'g')

    ax.view_init(40, 130)
    plt.show()


def draw_tri_surface(*points, n=20):
    u, v = gridspace(0, 1, n, d=2)

    surface = bernstein_bezier_tri_surface(*points)
    surface_pts = [[surface(x, y) for y in v if x + y <= 1]
                   for x in u]

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    draw_tri_mesh(surface_pts, ax, 'b')
    draw_tri_mesh(points, ax, 'r')
    draw_points(points, ax, 'g')

    plt.show()
