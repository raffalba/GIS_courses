from osgeo import gdal
from osgeo.gdalconst import *
import os, sys
import numpy

import time
##def main():
def run_script(iface): 

	# read all the values of the raster
	# -----------------------------------
	# registering driver
	gdal.AllRegister()

	# start timing
	startTime = time.time()

	# open the data source
	fn = '/home/user/Desktop/exercise2/DEM.Tiff'
	ds = gdal.Open(fn, GA_ReadOnly)
	if ds is None:
		print 'Could not open ' + fn
		sys.exit(1)

	cols = ds.RasterXSize
	rows = ds.RasterYSize
	bands = ds.RasterCount

	# list where we will save the raster bands
	# average value of the raster bands
	meanList = []
	# read bands and save in meanList (matricial form)
	for i in range(bands):
		band = ds.GetRasterBand(i+1)
		data = band.ReadAsArray(0, 0, cols, rows)
		AverageValue=numpy.mean(data)
		meanList.append(AverageValue)
		band = None
	ds=None

	meanArray=numpy.array(meanList)
	num=cols*rows*bands

	AverageValue=meanArray.mean()

	print 'Number of values=%d' % num
	print 'Average Value=%.2f' % AverageValue

	endTime = time.time()

	print 'The script has used ' + str(endTime - startTime) + ' seconds'



	pass





if __name__ == '__main__':
    iface=''
    run_script(iface)
##    main()
