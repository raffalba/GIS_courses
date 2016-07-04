## GFI - GeomorphicFloodIndex
## Hydrolab, University of Basilicata (http://www2.unibas.it/manfreda/HydroLab/home.html)
##Salvatore Manfreda, Caterina Samela, Raffaele Albano
## maito: raffaele.albano@unibas.it

from osgeo import gdal
from osgeo.gdalconst import *
import numpy
import matplotlib.pyplot as plt
import os,sys
import math

## to be runned via QGIS ScriptRunner
def run_script(iface):

## Required input data
## demvoid: raster Grid Digital Elevation Model
## demcon: hydrologically conditioned or filled Digital Elevation Model or Filled DEM
## FlowDir: Flow Direction
## FlowAcc: Flow accumulation
## G: slope

#set path dataset - Example dataset is Hilly areas - Big Sandy Guyandotte Basin
    file_demcon="/home/user/Desktop/GFI/1/INPUT_calibration/demcon_rit.txt"
    file_demvoid="/home/user/Desktop/GFI/1/INPUT_calibration/demvoid_rit.txt"
    file_flowdir="/home/user/Desktop/GFI/1/INPUT_calibration/flowdir_rit.txt"
    file_flowacc="/home/user/Desktop/GFI/1/INPUT_calibration/flowacc_rit.txt"
    file_slope='/home/user/Desktop/GFI/1/INPUT_calibration/slope_rit.txt'
    file_output='/home/user/Desktop/GFI/1/GFIrit.tif'

## A Standard Flood Map derived for a small portion of the basin of interest...
##...(not less than 2% of the basin) using detailed methods of analysis (e.g...
##...Hydraulic simulations. It will be used to calibrate the classifier

#register drivers to read input data
    gdal.AllRegister()
    print 'Opening ' + file_demcon
    ds_demcon = gdal.Open(file_demcon, GA_ReadOnly)
    if ds_demcon is None:
            print 'Could not open ' + file_demcon
            sys.exit(1)

    print 'Opening ' + file_demvoid
    ds_demvoid = gdal.Open(file_demvoid, GA_ReadOnly)
    if ds_demvoid is None:
            print 'Could not open ' + file_demvoid
            sys.exit(1)

    print 'Opening ' + file_flowdir
    ds_flowdir = gdal.Open(file_flowdir, GA_ReadOnly)
    if ds_flowdir is None:
            print 'Could not open ' + file_flowdir
            sys.exit(1)


    print 'Opening ' + file_flowacc
    ds_flowacc = gdal.Open(file_flowacc, GA_ReadOnly)
    if ds_flowacc is None:
            print 'Could not open ' + file_flowacc
            sys.exit(1)

    print 'Opening ' + file_slope
    ds_G = gdal.Open(file_slope, GA_ReadOnly)
    if ds_G is None:
            print 'Could not open ' + file_slope
            sys.exit(1)

#calculate slope(gdaldem)
##    print 'Calculating slope... '
##    if os.path.isfile('slope.tif'):
##        os.remove('slope.tif')
##    gdaldem_command="gdaldem slope "+ file_demcon+" slope.tif "
##    os.system(gdaldem_command)
##    print 'slope done'
##
##    print 'Opening slope'
##    ds_G = gdal.Open('slope.tif', GA_ReadOnly)
##    if ds_G is None:
##            print 'Could not open slope'
##            sys.exit(1)

    cols = ds_demcon.RasterXSize
    rows = ds_demcon.RasterYSize
    bands = ds_demcon.RasterCount

    geotransform = ds_demcon.GetGeoTransform()
    originX = geotransform[0]
    originY = geotransform[3]
    #pixelWidth = geotransform[1]
    cellsize = geotransform[5]

    print 'columns '+ str(cols)
    print 'rows '+ str(rows)
    print 'bands '+ str(bands)


    band_demcon=ds_demcon.GetRasterBand(1)
    demcon=band_demcon.ReadAsArray(0,0,cols,rows)

    band_demvoid=ds_demvoid.GetRasterBand(1)
    demvoid=band_demvoid.ReadAsArray(0,0,cols,rows)

    band_flowdir=ds_flowdir.GetRasterBand(1)
    flowdir=band_flowdir.ReadAsArray(0,0,cols,rows)

    band_flowacc=ds_flowacc.GetRasterBand(1)
    flowacc=band_flowacc.ReadAsArray(0,0,cols,rows)

    band_G=ds_G.GetRasterBand(1)
    G=band_G.ReadAsArray(0,0,cols,rows)
##    G=numpy.deg2rad(G);
    nanvalue=-9999

    # convert to float
    demcon=demcon.astype(numpy.float32)
    demvoid=demvoid.astype(numpy.float32)
    flowdir=flowdir.astype(numpy.float32)
    flowacc=flowacc.astype(numpy.float32)
    G=G.astype(numpy.float32)
    G[G==nanvalue]=numpy.nan
    demcon[demcon==nanvalue]=numpy.nan
    demvoid[demvoid==nanvalue]=numpy.nan
    flowdir[flowdir==nanvalue]=numpy.nan
    flowacc[flowacc==nanvalue]=numpy.nan
    #numpy.savetxt('dem_python.txt',demcon)

## Identification of the Drainage Network
    dem=numpy.copy(demcon)

    #numpy.savetxt('dem_python.txt',dem)

    a=rows
    b=cols

    dem[numpy.isnan(dem)]=100000

    channel=numpy.zeros( (rows,cols))

    tmp=flowacc*numpy.square(cellsize)*numpy.power( (G+0.0001), 1.7)
    c1=tmp<40000
    c2=tmp>30000
    channel[c1*c2 ]=1

    #numpy.savetxt('flowdir_python.txt',flowdir)
    #numpy.savetxt('flowacc_python.txt',flowacc)
    #numpy.savetxt('G_python.txt',G)
    #numpy.savetxt('channel_python.txt',channel)
    #for ctr in range(0,rows):
    #    print ctr
    #    for ctc in range(0,cols):
    #        tmp= flowacc[ctr,ctc]*numpy.square(cellsize)*numpy.power( (G[ctr,ctc]+0.0001), 1.7)
    #        if tmp < 40000 and tmp >30000:
    #            channel[ctr,ctc]=1
    for ctr in range(1,rows-2):
        print ctr
        for ctc in range(1,cols-2):
            if channel[ctr,ctc]>0:
                x=ctr;
                y=ctc;
                while dem[x,y]<10000 and x < a-2 and x>0 and y<b-2 and y>0:
                    fd=flowdir[x,y]
                    if fd==1:
                        x=x
                        y=y+1
                    if fd==128:
                        x=x-1
                        y=y+1
                    if fd==64:
                        x=x-1
                        y=y
                    if fd==32:
                        x=x-1
                        y=y-1
                    if fd==16:
                        x=x
                        y=y-1
                    if fd==8:
                        x=x+1
                        y=y-1
                    if fd==4:
                        x=x+1
                        y=y
                    if fd==2:
                        x=x+1
                        y=y+1
                    if channel[x,y]==2:
                        break
                    else:
                        channel[x,y]=2

## Calculation of the "Ariver": the contributing area in the nearest section of the drainage network...
##...hydrologically connected to the point under exam.
##...Calculation of the Elevation difference (H) to the nearest channel

    dem=numpy.copy(demcon)
    #numpy.savetxt('channel_python2.txt',channel)
    #numpy.savetxt('dem_python.txt',dem)
    H=numpy.zeros((rows,cols))
    Ariver=numpy.zeros((rows,cols))
    for ctr in range(1,rows-2):
        print ctr
        for ctc in range(1,cols-2):
            if dem[ctr,ctc]<10000:
                x=ctr
                y=ctc
                Ld=0
                dm=0
                sqrt2=numpy.sqrt(2)
                while channel[x,y]==0 and x< a-2 and x>0 and y<b-2 and y>0 and flowdir[x,y]>-9999:
                    fd=flowdir[x,y]

                    if fd==1:
                        x=x
                        y=y+1
                        Ld=Ld+cellsize
                    if fd==128:
                        x=x-1
                        y=y+1
                        Ld=Ld + cellsize*sqrt2
                    if fd==64:
                        x=x-1
                        y=y
                        Ld=Ld + cellsize
                    if fd==32:
                        x=x-1
                        y=y-1
                        Ld=Ld + cellsize*sqrt2
                    if fd==16:
                        x=x
                        y=y-1
                        Ld=Ld + cellsize
                    if fd==8:
                        x=x+1
                        y=y-1
                        Ld=Ld + cellsize*sqrt2
                    if fd==4:
                        x=x+1
                        y=y
                        Ld=Ld + cellsize;
                    if fd==2:
                        x=x+1
                        y=y+1
                        Ld=Ld + cellsize*sqrt2

                Ariver[ctr,ctc]=flowacc[x,y]
                H[ctr,ctc]=dem[ctr,ctc]-dem[x,y]
    H[numpy.isnan(demvoid)]=numpy.nan
    Ariver[ctr+1,:]=0;
    Ariver[:,ctc+1]=0;
    H[H==0]=0.00001
    #Estimation of the water depth in the nearest element of the drainage network...
    #...connected to the location under exam using an hydraulic scaling relation (Leopold and maddock, 1953)
    #...h=aA^n

    #% Parameters estimated for the Ohio River basin:
    a = 0.1035
    n = 0.4057
    #% hydraulic scaling relation (A[km^2])

    hr = a*numpy.power((((Ariver+1)*cellsize*cellsize)/1000000),n);

    #%% Index GFI=ln[hr/H]
    hronH=hr/H;
    ln_hronH=numpy.real(numpy.log(hronH));



    #numpy.savetxt('Ariver.txt',Ariver)
    #numpy.savetxt('H.txt',H)
    #numpy.savetxt('hr.txt',hr)
    #numpy.savetxt('ln_hronH.txt',ln_hronH)



## plot all dataset (input-intermediate-output)
    plt.figure(1)
    plt.subplot(1,3,1)
    plt.imshow(demcon)
    plt.title('DEM')
    plt.colorbar()

    plt.subplot(1,3,2)
    plt.imshow(flowdir)
    plt.title('Flow Direction')
    plt.colorbar()

    plt.subplot(1,3,3)
    plt.imshow(flowacc)
    plt.title('Flow Accumulation')
    plt.colorbar()

    plt.figure(2)
    plt.subplot(2,2,1)
    plt.imshow(channel)
    plt.title('CHANNEL')
    plt.colorbar()

    plt.subplot(2,2,2)
    plt.imshow(H)
    plt.title('Elevation difference H')
    plt.colorbar()

    plt.subplot(2,2,3)
    plt.imshow(Ariver)
    plt.title('Contributing area A_{river}')
    plt.colorbar()

    plt.subplot(2,2,4)
    plt.imshow(ln_hronH)
    plt.title('Geomorphic Flood Index ln(h_r/H)')
    plt.colorbar()

    plt.show()


    #Export output

    driver1=gdal.GetDriverByName('GTiff')
    driver1.Register()
    #file_output='GFI.tif'
    target_ds=driver1.Create(file_output,cols,rows,1,gdal.GDT_Float32)
    target_ds.SetGeoTransform(geotransform)
    band_target=target_ds.GetRasterBand(1)
    band_target.WriteArray(ln_hronH)
    band_target.FlushCache()
    band_target=None
    target_ds=None

    band_demcon=None
    ds_demcon=None

    band_demvoid=None
    ds_demvoid=None

    band_flowdir=None
    ds_flowdir=None

    band_flowacc=None
    ds_flowacc=None

    band_G=None
    ds_G=None


##  to be runned via QGIS ScriptRunner
if __name__ == '__main__':
    iface=''
    run_script(iface)



