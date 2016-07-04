Geomorpholgical Approach for delineation of flood prone areas: The GeomorphicFloodIndex, i.e. a new linear binary classifier

GeomorphicFloodIndex - GFI = ln(hr /H) 
This index aims to compare in each point a variable water depth h with the elevation difference H, where h is calculated for each basin cell assuming a scaling relationship with the contributing area (Ar)in the section of the drainage network (‘r’ stands for river) hydrologically connected to the point under exam.
This index could be extremely useful for flood hazard mapping in Large Region and Ungauged Basin.

1. Open ScriptRunner Plugin and add the script “GeomorphicFloodIndex_scriptrunner_v1.py”
2. Check the path of the input files and run the script on the calibration area.
3. Open the results of output raster file GFI_rit.tif in QGIS and classify the raster with a color graduation scale. 
4. Firstly, you can perform a visual comparison with the standard flood map “floodhazard100y_rit.txt” to check which is the value of the GFI index (i.e. treshold) that performs better (i.e. overlays) the extent of the standard map. 
You could create a script to compare map obtained by hydraulic simulation depicted to the potential flood-prone areas predicted by the geomorphic method in terms of total error = false positive + false negative.
5. You can run now the model on the validation area (Check the path of the validation input files) and use the map calculator tool to create a binary file in which the raster has value equal to 1 for the flooded area and 0 for the “un-flooded” cells: GFI_def > threshold
