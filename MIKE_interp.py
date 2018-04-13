#!/usr/bin/env python
# author: Thor Meinert Sundahl, s160158@student.dtu.dk
#
# usage: call MIKE_interp.py with arguments like so
# python MIKE_interp.py dem.tif mesh_f.mesh mesh_i.mesh
# dem.tif is GeoTIFF image, mesh_f.mesh is a MIKE formatted flat mesh file,
# mesh_i.mesh is the interpolated output mesh file
#
# REQUIRED: Python 64 bit for memory, gdal, scipy, numpy
from __future__ import division

import sys

from interp import interp, interp_mesh

def main(dem, mesh_f, mesh_i):
    f = interp(dem)
    interp_mesh(mesh_f, mesh_i, f)

if __name__=='__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3])
