Getting started with automatization in QGIS: run algorithm in batch mode through processing
Processing Framework provides an environment within QGIS to run native and third-party algorithms for processing data. It contains a batch processing interface that allows one to execute an algorithm on several layers easily. 
Batch processing is a useful tool that can save manual effort and help you automate repetitive tasks.
We will create several sub-basins from different outlets using the single processing batch command, i.e. r.water.oulet algortihm of GRASS GIS 7.

1. Activate the Processing pliugin; Open the Processing toolbox.
2. Add the GRASS GIS 7 algorithms in the processing toolbox (Use the processing advanced interface)
3. Search from r.water.outlet and click on the selected algorithm. Use the DEM_90.tif, the coordinate of one of the interest point ("punti_interesse.csv") as inputs, and use 90m as region cell size (as the input DEM reaster).
Run the algorithm and check the result raster file i.e. the created sub-basin. 
4. Search from r.water.outlet and click with the right mouse botton on the selected algorithm and select exsecute as batch process.
Use the same input options as before but use the coordinate of each outlet points for each of the 3 rows of the form. 
The algorithm will run for each of the inputs and create output files are we have specified, i.e. 3 basins for the 3 output outlets. Once the batch process finishes, you will see the layers added to QGIS canvas.