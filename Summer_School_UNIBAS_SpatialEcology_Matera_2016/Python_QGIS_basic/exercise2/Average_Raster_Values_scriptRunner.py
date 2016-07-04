from osgeo import gdal
from osgeo.gdalconst import *
import os, sys
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
	bandList = []
	# read bands and save in bandList (matricial form)
	for i in range(bands):
		band = ds.GetRasterBand(i+1)
		data = band.ReadAsArray(0, 0, cols, rows)
		bandList.append(data)

	Average=0.0
	num=0
	for k in range(bands):
		data = bandList[k]
		for i in range(rows):
			for j in range(cols):
				num=num+1
				
				# read each value of the matrix 
				value = data[i, j]
				Average=Average+value

	AverageValue=Average/num

	print 'Number of values=%d' % num
	print 'Average Value=%.2f' % AverageValue

	endTime = time.time()

	print 'The script has used ' + str(endTime - startTime) + ' seconds'


	pass





if __name__ == '__main__':
    iface=''
    run_script(iface)
##    main()


