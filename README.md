# Bezier
## Description
This project contains a Python3.6 module for generating and drawing Bézier curves and surfaces. It uses Bernstein polynomials, but an implementation of curves using the direct Casteljau algorithm is provided as a curiosity, despite that it has a greater computational complexity.


## Usage
The `bezier` module exports some functions, briefly explained here.

### `curve` and `curve2`
The `curve` function takes two or more 2-tuples (2D points) and returns a function which is the corresponding parametric Bézier curve of that control points. The `curve2` function is the same, but it internally uses a direct implementation of the Casteljau algorithm.

### `surface` and `tri_surface`
The `surface` function takes two or more lists of `m` 3-tuples (3D points), with m >=2, and returns a function which is the corresponding parametric Bézier surface of that mesh of control points. The `tri_surface` function is the same, but it takes a triangular 3D points mesh instead (see `examples/examples.py`).

### `draw` methods
The `draw_curve`, `draw_curve2`, `draw_surface` and `draw_tri_surface` methods act as the corresponding explained above, but they draw the curve/surface instead of returning a parametric function. 

The draw accurateness can be specified with an optional argument: `epsilon` for curves and `n` for surfaces. In the curve case, `epsilon` value is between 0 and 1. 1 for no accuracy at all and 0 for infinite accuracy (not recommended value).

## Examples
There are some drawing examples in `examples/examples.py`.

<p align="center">
  <img src="examples/curve.png" width="600px" height="600px">
</p>

<p align="center">
  <img src="examples/surface1.png" width="600px" height="600px">
</p>

<p align="center">
  <img src="examples/surface2.png" width="600px" height="600px">
</p>

<p align="center">
  <img src="examples/surface3.png" width="600px" height="600px">
</p>
