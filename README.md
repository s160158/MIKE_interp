# MIKE_interp

Complements MIKE Mesh Generator. Solves the problem of interpolating very large DEM files causing MIKE Mesh Generator to crash. MIKE_interp uses GDAL and numpy to interpolate flat mesh files by opening these up and replacing the height (z = 0) of every point by the interpolated value.

REQUIRES 64 bit version of Python to support larger (> 2 GB or so) memory storage.

# Usage
Call example

```
python MIKE_interp.py dem.tif in.mesh out.mesh
```

Takes 3 paramters: a GeoTIFF DEM of the region covering all points in in.mesh, in.mesh is a flat MIKE mesh file to be interpolated. The output, out.mesh, is the interpolated MIKE mesh file.

Another way to use this program is by editing the `interp.py` file to fit specific needs, this makes it possible to interpolate multiple files with the generated interpolator object. Very useful.
