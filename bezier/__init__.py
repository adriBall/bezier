from .casteljau import casteljau_bezier_curve as curve2
from .bernstein import bernstein_bezier_curve as curve, bernstein_bezier_surface as surface, \
    bernstein_bezier_tri_surface as tri_surface
from .draw_surface import draw_surface, draw_tri_surface
from .draw_curve import casteljau_draw_bezier as draw_curve2, bernstein_draw_bezier as draw_curve

__all__ = ['curve2', 'curve', 'surface', 'tri_surface', 'draw_curve', 'draw_curve2',
           'draw_surface', 'draw_tri_surface']
