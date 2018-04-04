# genice-diffr

A [GenIce](https://github.com/vitroid/GenIce). plugin for visualizing the structure factor in 3D.

## Installation

### System-wide installation

(Not working)

    % pip install genice-diffr
	
or

    % make install

### Private installation

Copy the files in genice/formats into your local formats folder of GenIce.

## Requirement

* [GenIce](https://github.com/vitroid/GenIce).

## Usage

	% genice iceR -r 3 3 3 -f _DIffr[25.0,50.0] > iceR.diffr.yap
	% iceR.diffr.yap

[25.0,50.0] are the threshold values for rendering the contour.  Default value is 5.0.

## Test in place

    % make test
    % yaplot iceR.diffr.yap

Currently, the output format is in [Yaplot](https://github.com/vitroid/Yaplot).
