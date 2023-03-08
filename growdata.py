# #!/usr/bin/python
# from mpl_toolkits.basemap import Basemap
# import matplotlib.pyplot as plt
# import numpy as np

# # input desired coordinates
# my_coords = [38.9719980,-76.9219820]

# # How much to zoom from coordinates (in degrees)
# zoom_scale = 1

# # Setup the bounding box for the zoom and bounds of the map
# bbox = [my_coords[0]-zoom_scale,my_coords[0]+zoom_scale,\
#         my_coords[1]-zoom_scale,my_coords[1]+zoom_scale]

# plt.figure(figsize=(12,6))
# # Define the projection, scale, the corners of the map, and the resolution.
# m = Basemap(projection='merc',llcrnrlat=bbox[0],urcrnrlat=bbox[1],\
#             llcrnrlon=bbox[2],urcrnrlon=bbox[3],lat_ts=10,resolution='i')

# # Draw coastlines and fill continents and water with color
# m.drawcoastlines()
# m.fillcontinents(color='peru',lake_color='dodgerblue')

# # draw parallels, meridians, and color boundaries
# m.drawparallels(np.arange(bbox[0],bbox[1],(bbox[1]-bbox[0])/5),labels=[1,0,0,0])
# m.drawmeridians(np.arange(bbox[2],bbox[3],(bbox[3]-bbox[2])/5),labels=[0,0,0,1],rotation=45)
# m.drawmapboundary(fill_color='dodgerblue')

# # build and plot coordinates onto map
# x,y = m(my_coords[1],my_coords[0])
# m.plot(x,y,marker='D',color='r')
# plt.title("Geographic Point Test")
# plt.savefig('coordinate_test.png', format='png', dpi=500)
# plt.show()


#!/usr/bin/python
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import csv

lats, lons,names,altitude = [],[],[],[]

with open('asos_stations.csv') as csvfile:
    reader = csv.DictReader(csvfile,delimiter=',')
    for data in reader:
        names.append(data['CALL'])
        lats.append(float(data['LAT']))
        lons.append(float(data['LON']))
        altitude.append(float(data['ELEV']))

# How much to zoom from coordinates (in degrees)
zoom_scale = 0

# Setup the bounding box for the zoom and bounds of the map
bbox = [np.min(lats)-zoom_scale,np.max(lats)+zoom_scale,\
        np.min(lons)-zoom_scale,np.max(lons)+zoom_scale]

plt.figure(figsize=(12,6))
# Define the projection, scale, the corners of the map, and the resolution.
m = Basemap(projection='merc',llcrnrlat=bbox[0],urcrnrlat=bbox[1],\
            llcrnrlon=bbox[2],urcrnrlon=bbox[3],lat_ts=10,resolution='i')

# Draw coastlines and fill continents and water with color
m.drawcoastlines()
m.fillcontinents(color='peru',lake_color='dodgerblue')

# draw parallels, meridians, and color boundaries
m.drawparallels(np.arange(bbox[0],bbox[1],(bbox[1]-bbox[0])/5),labels=[1,0,0,0])
m.drawmeridians(np.arange(bbox[2],bbox[3],(bbox[3]-bbox[2])/5),labels=[0,0,0,1],rotation=45)
m.drawmapboundary(fill_color='dodgerblue')

# build and plot coordinates onto map
x,y = m(lons,lats)
m.plot(x,y,'r*',markersize=5)
plt.title("Plotting Grow Dataset")
plt.savefig('Grow_dataset.png', format='png', dpi=500)
plt.show()