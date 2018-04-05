# genice-diffr

A [GenIce](https://github.com/vitroid/GenIce) plugin for visualizing the structure factor in 3D.

## Requirements

    % make prepare
will install required packages via pip.

* [GenIce](https://github.com/vitroid/GenIce) >=0.16.
* [yaplotlib](https://github.com/vitroid/yaplotlib) >=0.1.

## Installation

### System-wide installation

Not supported.

### Private installation

    % make install
or copy the files in formats/ into your local formats folder of GenIce.

## Usage

	% genice 1c -r 3 3 3 -f _Diffr[25.0,50.0] > 1c.diffr.yap
	% yaplot 1c.diffr.yap

[25.0,50.0] are the threshold values for rendering the contour.  Default value is 5.0.
Currently, the output format is in [Yaplot](https://github.com/vitroid/Yaplot).

## Test in place

    % make test
    % yaplot iceR.diffr.yap

