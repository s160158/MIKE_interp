#!/usr/bin/env python
from __future__ import division

from osgeo import gdal
import numpy as np
from scipy import interpolate

def interp(dem):
    """
    Generate an interpolator object
    :param dem:
    :return:
    """
    ds = gdal.Open(dem, gdal.GA_ReadOnly)
    # Get the resolution of the input raster
    transform = ds.GetGeoTransform()

    arr_z = np.array(ds.GetRasterBand(1).ReadAsArray())  # only one band - DEM

    ds = None

    x = np.arange(transform[0], transform[0] + arr_z.shape[1] * transform[1], transform[1])
    y = np.arange(transform[3], transform[3] + arr_z.shape[0] * transform[5], transform[5]) # sometimes it length is not equal arr_z

    print x.shape
    print y.shape
    print arr_z.shape

    print 'Interpolating...'

    f = interpolate.interp2d(x[0:arr_z.shape[1]], y[0:arr_z.shape[0]], arr_z, kind='cubic')

    return f

def interp_mesh(filename, filename_out, f):
    """
    Interpolate a flat MIKE mesh using an interpolator object f
    :param filename:
    :param filename_out:
    :param f:
    :return:
    """
    fh = open(filename, 'r')
    fh_out = open(filename_out, 'w')

    i = 1
    N = 100 # arbitrary > 1
    for line in fh:
        if i == 1:
            N = int(line.split('  ')[2])  # number of nodes in mesh
            fh_out.write(line)  # keep the header!
        elif i > N + 1:
            fh_out.write(line)  # mesh information. Unchanged!
        else:
            x = float(line.split(' ')[1])
            y = float(line.split(' ')[2])
            z = f(x, y)[0]

            line_out = line.split(' ')
            line_out[3] = str(z)

            fh_out.write(' '.join(line_out))
            print '[*] - Node: {} : (x, y, z) = ({}, {}, {})'.format(line.split(' ')[0], x, y, z)

        i += 1

    fh.close()
    fh_out.close()





if __name__=='__main__':
    #interp('./test/mesh.mesh', './test/mesh_interp.mesh', './test/mesh.tif')

    f = interp('C:/Users/thsu/Desktop/thesis/cornerbox/extract/box722183_6185596/e/box_34672x28512_r004x004.tif')

    #interp_mesh('C:/Users/thsu/Desktop/thesis/quad_meshes/mesh_local/box_02816x02816_008x008_01_flat.mesh', 'C:/Users/thsu/Desktop/thesis/quad_meshes/mesh_local/box_02816x02816_008x008_01_interp.mesh', f)

    interp_mesh('C:/Users/thsu/Desktop/thesis/quad_meshes/mesh_regional/box_34672x28512_032x024_02_flat.mesh', 'C:/Users/thsu/Desktop/thesis/quad_meshes/mesh_regional/box_34672x28512_032x024_02.mesh', f)
    interp_mesh('C:/Users/thsu/Desktop/thesis/quad_meshes/mesh_regional/box_34672x28512_064x052_02_flat.mesh', 'C:/Users/thsu/Desktop/thesis/quad_meshes/mesh_regional/box_34672x28512_064x052_02.mesh', f)
    interp_mesh('C:/Users/thsu/Desktop/thesis/quad_meshes/mesh_regional/box_34672x28512_064x052_03_flat.mesh', 'C:/Users/thsu/Desktop/thesis/quad_meshes/mesh_regional/box_34672x28512_064x052_03.mesh', f)
    interp_mesh('C:/Users/thsu/Desktop/thesis/quad_meshes/mesh_regional/box_34672x28512_132x108_03_flat.mesh', 'C:/Users/thsu/Desktop/thesis/quad_meshes/mesh_regional/box_34672x28512_132x108_03.mesh', f)
    interp_mesh('C:/Users/thsu/Desktop/thesis/quad_meshes/mesh_regional/box_34672x28512_132x108_04_flat.mesh', 'C:/Users/thsu/Desktop/thesis/quad_meshes/mesh_regional/box_34672x28512_132x108_04.mesh', f)
