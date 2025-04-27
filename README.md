This program generates a basic map of the globe and then creates a heatmap of active wildfires over it using data from a CSV file obtained from MODIS.

The program utilizes a few Python modules that are imported at the beginning of the code: 
The CSV module, for reading and utilizing data from the CSV file. 
The GeoPandas module, for obtaining and displaying a basic map of the globe. 
Pyplot from Matplotlib to plot the heatmap of wildfires over the globe. 
Numpy, solely to use the histogram2d function to help generate a 2-dimensional heatmap over the globe map. 

The program then generates 3 lists of data from the CSV file: Latitude, Longitude, and Intensities of the wildfires in each row of the CSV file. 
A heatmap is generated using these values and is then overlayed on top of the worldmap image generated using GeoPandas. 

I'm still a bit of an amateur when it comes to Python so I did run into a problem separating the heatmap's coloration from the base global map. If you run this code you will notice that the globe ends up with a dark gray hue due to the heatmap coloration being applied to it. 
Without the heatmap the globe actually appears white in color with only black lines to draw out continents and island shapes. I'm still working through how I can separate the coloration of these two out. 
