import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

df = pd.read_csv('cities.csv')

geometry = gpd.points_from_xy(df['Longitude'], df['Latitude'])
gdf = gpd.GeoDataFrame(df, geometry=geometry)

world = gpd.read_file('ne_110m_admin_0_countries.shp')

fig, ax = plt.subplots(figsize=(10, 8))
world.plot(ax=ax, color='lightblue', edgecolor='black')
gdf.plot(ax=ax, color='red', markersize=50)

# Add labels or annotations as needed
for index, row in gdf.iterrows():
    ax.annotate(row['City'], xy=(row.geometry.x, row.geometry.y), ha='center', va='center')

plt.title('Cities on a World Map')
plt.show()
