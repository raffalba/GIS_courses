Getting started with Python in QGIS: works with raster
We will use the QGIS plugin "ScriptRunner" to run a python script (Average_Raster_Values_scriptRunner.py) that reads all the values of a raster file of ground elevation (DEM. TIFF) and calculated the mean value.
Moreover, we will visualize the computational time utilized to run the script and we will compare it with another script that use the Numpy library (Average_Raster_Value_Numpy_scriptRunner.py) that is specific to works with big matrices.

1. Firstly open the script "Average_Raster_Values_scriptRunner.py" with a text editor and substitute the path of the raster "DEM.TIFF" (check rows n.19) with the one in which you have stored the file.
2. Open the QGIS project called "MappaRaster.qgs" 
3. In the "Plugin" menu, choose "Manage and Install Plugins" and search for "Scriptrunner". Finally select "Install plugin" in the bottom part of the form.
4. Open "ScriptRunner" and select "Add a Python Script". Select and Run the script "Average_Raster_Values_scriptRunner.py".
5. You can do the same procedure for the script "Average_Raster_Value_Numpy_scriptRunner.py" and check the results, in particular, the computational time used for the two different script.