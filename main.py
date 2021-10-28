import pandas as pd
import numpy  as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap


air = pd.read_csv("C:/Users/blair/Desktop/data/Full_Merge_of_All_Unique Airports.csv", encoding='gbk') #Airport  data
flights = pd.read_csv("C:/Users/blair/Desktop/data/DRAW_ROUTES.csv", encoding='gbk')# Route Data

fig = plt.figure(figsize=(16, 12))
ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
map = Basemap()
map.shadedrelief(scale=0.1)
map.drawparallels(circles=np.linspace(-90, 90, 7),
                  labels=[1, 0, 0, 0], color='gray')
map.drawmeridians(meridians=np.linspace(-180, 180, 13),
                  labels=[0, 0, 0, 1], color='gray')

# Define a function that outlines the line segment between two points：

'''def create_great_circles(df):
    for index,row in df.iterrows():
        start_lon = row['start_longitude']
        start_lat = row['start_latitude']
        end_lon = row['end_longitude']
        end_lat = row['end_latitude']
        if abs(end_lat - start_lat) < 180 and abs(end_lon - start_lon) < 180:
            map.drawgreatcircle(start_lon, start_lat, end_lon, end_lat, linewidth=0.03
                                ,color = "#DF666A")
# Execute the route drawing function
create_great_circles(flights)'''
# Define a function to fill the scatter plot with colour, size：

def create_great_points(df):
    lon = np.array(df["Longitude"])
    lat = np.array(df["Latitude"])
    x, y = map(lon, lat)
    for lon, lat in zip(x, y):
        map.scatter(lon, lat, marker="o", s=1, color="#DF666A")
# Execute the scatter plot fill function
create_great_points(air)
#SaveImage
plt.savefig('D:/route.png', dpi=100, bbox_inches='tight')
plt.show()