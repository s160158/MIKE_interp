# MIKE_interp

Complements MIKE Mesh Generator. Solves the problem of interpolating very large DEM files causing MIKE Mesh Generator to crash. MIKE_interp uses GDAL and numpy to interpolate flat mesh files by opening these up and replacing the height (z = 0) of every point by the interpolated value.

REQUIRES 64 bit version of Python to support larger (> 2 GB or so) memory storage.
