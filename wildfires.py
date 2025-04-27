#importing all of the modules needed for the program

import csv
import geopandas as gpd
from matplotlib import pyplot as plt
import numpy as np

url = "https://naciscdn.org/naturalearth/110m/cultural/ne_110m_admin_0_countries.zip" #grabbing the image to use as the world map
filename = "MODIS_C6_1_Global_24h.csv" #grabbing the csv file with wildfire data 


gdf = gpd.read_file(url)
fig = plt.figure(figsize=(30, 20))
ax = fig.add_subplot()

# plots a basic map of the world
gdf.plot(
    ax=ax,
    color="lightgray",
    edgecolor="black",
    alpha=0.2
)

# turn off axis ticks
ax.set_xticks([])
ax.set_yticks([])

#create empty lists for data from csv 
lats, lons, intensities = [], [], []

#this grabs the relevant data for plotting the fires on the globe and getting their intensity/brightness
with open("MODIS_C6_1_Global_24h.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)  # Skips header row in csv file
    #This iterates through the CSV files and grabs data regarding the location of the fires and how intense they area. 
    for row in reader:
            lat = float(row[0])  
            lon = float(row[1])  
            intensity = float(row[2])  
            lats.append(lat)
            lons.append(lon)
            intensities.append(intensity)



# heatmap creation
heatmap, xedges, yedges = np.histogram2d(lons, lats, bins=[250, 250], weights=intensities)



plt.imshow(heatmap.T, origin="lower", cmap="hot", extent=[min(lons), max(lons), min(lats), max(lats)], alpha=0.8)


#plot initialization

plt.colorbar(label="Wildfire Intensity")

plt.title("Global Wildfire Heatmap")

plt.show()
