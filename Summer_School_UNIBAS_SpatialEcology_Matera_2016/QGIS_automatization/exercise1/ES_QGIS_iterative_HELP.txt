Getting started with automatization in QGIS: run algorithm in interative mode through processing
Processing Framework provides an environment within QGIS to run native and third-party algorithms for processing data. It contains an iterative processing interface that allows one to execute e.g. an algorithm that use vector layers, by running them repeatedly, iterating over the features in an input vector layer. 
Iterative processing is a useful tool that can save manual effort and help you automate repetitive tasks.
We will clip a DEM on each feature of a layers that contains set of watersheds.  That will be useful if you later want to calculate some parameters related to each watershed, such as its mean elevation or it hypsographic curve.
The exercize and its data are taken from the QGIS documentation available on the web at http://docs.qgis.org/2.8/en/docs/training_manual/

1. Activate the Processing pliugin; Open the Processing toolbox.
2. Search for "clip grid with polygon" (GDAL algorthm)
3. Execute the algortihms with dem25.tif and watersheds.shp as inputs. As you can see, the result is an area that is covered by all the watershed polygons used.
4. Select one feature and esecute clip grid with polygon algorithm. Since only selected features are used, only the selected polygon will be used to crop the raster layer.
5. First of all, remove the previous selection, so all polygons will be used again. Now open the Clip grid with polygon algorithm and select the same inputs as before, but this time click on the button that you will find in the right–hand side of the vector layer input where you have selected the watersheds layer.
Then, enter an output filename, resulting files will be named using that filename and a number corresponding to each iteration as suffix.
the results will be a set of raster layers, each one of them corresponding to one of the executions of the algorithm
