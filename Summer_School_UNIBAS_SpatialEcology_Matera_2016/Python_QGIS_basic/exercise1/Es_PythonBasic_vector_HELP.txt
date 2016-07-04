Getting started with Python in QGIS: works with vectors
We will load a vector point layer representing all schools and use python scripting to create a text file with the school name, code, latitude and longitude for each of the school in the layer.

1. In the "Layer" menu, select "Add Vector Layer" e browse the path in which you have stored the file "schools_it.sph", i.e. . You can dowlnolad this vector layer at http://www.pcn.minambiente.it/GN/accesso-ai-servizi/servizi-di-download/wfs as wfs service.
2. Select the botton "Indentify Resuts" and click on a point of the uploaded layer. Now, you can visualize the attributes linkes to thuis feature (point geometry). In particular, you will visualize name and code, respectively "denominazi" and cod_istitu".
3. In the "Plugins" manu, you can select "Python Console". Once, it has been appeared after the canvas, we can work in the prompt in the bottom part of the form.
4. To access the currently active layer in QGIS, you can type the following and press "Enter": layer = iface.activeLayer()
5. you can run the following command to see what operations we can do on the layer variable: dir(layer)
6. Among the long list of functions available, we can work with getFeatures() to get the reference to all features of a layer: 

for f in layer.getFeatures():
  print f

Make sure to add 2 spaces before typing the second line.
7.  We can use the f variable to access the attributes of each feature. Type the following to print the name (i.e. "denominazi") and and code ("cod_istitu") for each school feature.

for f in layer.getFeatures():
  print f['denominazi'], f['cod_istitu']


8. Now to access to the coordinates of the feature:

for f in layer.getFeatures():
  geom = f.geometry()
  print geom.asPoint()

9. if we wanted to get only the x cordinate of the feature:

for f in layer.getFeatures():
  geom = f.geometry()
  print geom.asPoint().x()

10. Type the following code to print the name, iata_code, latitude and longitude of each of the airport features:

for f in layer.getFeatures():
  geom = f.geometry()
  print '%s, %s, %f, %f' % (f['denominazi'], f['cod_istitu'],
         geom.asPoint().y(), geom.asPoint().x())

The %s and %f notations are ways to format a string and number variables.

11. Finally, type the following code to store the output would be in a file:

output_file = open('/home/user/Desktop/exercise1/schools_it.txt', 'w')
for f in layer.getFeatures():
  geom = f.geometry()
  line = '%s, %s, %f, %f\n' % (f['denominazi'], f['cod_istitu'],
          geom.asPoint().y(), geom.asPoint().x())
  unicode_line = line.encode('utf-8')
  output_file.write(unicode_line)
output_file.close()

Please, check and set the path of the output file on your pc.

