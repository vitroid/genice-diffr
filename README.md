# genice-diffr

A [GenIce](https://github.com/vitroid/GenIce) plugin for visualizing the structure factor in 3D.

## Requirements

* [GenIce](https://github.com/vitroid/GenIce) >=0.23.
* [yaplotlib](https://github.com/vitroid/yaplotlib) >=0.1.
* [contour3d](https://github.com/vitroid/contour3d) >=0.1.

## Installation

### System-wide installation

    % make install

### Private installation

Copy the files in genice_diffr/formats/ into your local formats folder of GenIce.

## Usage

	% genice 1c -r 3 3 3 -f _Diffr[25.0,50.0] > 1c.diffr.yap
	% yaplot 1c.diffr.yap

[25.0,50.0] are the threshold values for rendering the contour.  Default value is 5.0.
Currently, the output format is in [Yaplot](https://github.com/vitroid/Yaplot).

## Test in place

    % make test
    % yaplot iceR.diffr.yap

