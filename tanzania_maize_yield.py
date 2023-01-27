import pandas as pd
import geopandas as gpd
from bokeh.io import output_file, show
from bokeh.plotting import figure
from bokeh.models import GeoJSONDataSource, ColumnDataSource, HoverTool
from bokeh.palettes import Viridis256
from bokeh.layouts import gridplot
from bokeh.models import LinearColorMapper, ColorBar

# Read the shapefiles
unimodal_shapefile = gpd.read_file("unimodal.shp")
country_shapefile = gpd.read_file('tanzania.shp')

# Read and merge the csv file
yield_data = pd.read_csv("districts_points2.csv")

# convert yield (kg/ha) to MT/Ha
yield_data['gwad'] = yield_data['gwad']/1000

#Merge the dataframes
merged_data = pd.merge(unimodal_shapefile, yield_data, on="NAME_2")

# convert to geojson
geo_source = GeoJSONDataSource(geojson=merged_data.to_json())
country_geo_source = GeoJSONDataSource(geojson=country_shapefile.to_json())

# Plotting the first map
p1 = figure(title='2023 MAM Season yield (MT/Ha)', outer_width=600, outer_height=600)

color_mapper = LinearColorMapper(palette=Viridis256, low=min(merged_data['gwad']), high=max(merged_data['gwad']))

p1.multi_line('xs','ys', source=country_geo_source,line_color='black', line_width=0.5)

p1.patches('xs','ys', source=geo_source,
          fill_color={'field': 'gwad', 'transform': color_mapper},
          fill_alpha=0.7, line_color='black', line_width=0.5)


hover = HoverTool(tooltips=[('District', '@NAME_2'), ('Yield', '@gwad')])
p1.add_tools(hover)


color_bar = ColorBar(color_mapper=color_mapper, label_standoff=8, width=20, height=300,
                     border_line_color=None, location=(0,0), orientation='vertical')
p1.add_layout(color_bar, 'right')

# Plotting the second map
p2 = figure(title='2022 MAM Season yield (MT/Ha)', outer_width=600, outer_height=600)

color_mapper = LinearColorMapper(palette=Viridis256, low=min(merged_data['gwad']), high=max(merged_data['gwad']))

p2.multi_line('xs','ys', source=country_geo_source,line_color='black', line_width=0.5)

p2.patches('xs','ys', source=geo_source,
          fill_color={'field': 'gwad', 'transform': color_mapper},
          fill_alpha=0.7, line_color='black', line_width=0.5)


hover = HoverTool(tooltips=[('District', '@NAME_2'), ('Yield', '@gwad')])
p2.add_tools(hover)


color_bar = ColorBar(color_mapper=color_mapper, label_standoff=8, width=20, height=300,
                     border_line_color=None, location=(0,0), orientation='vertical')
p2.add_layout(color_bar, 'right')

#Plotting the third map
p3 = figure(title='2022 OND Season yield (MT/Ha)', outer_width=600, outer_height=600)

color_mapper = LinearColorMapper(palette=Viridis256, low=min(merged_data['gwad']), high=max(merged_data['gwad']))

p3.multi_line('xs','ys', source=country_geo_source,line_color='black', line_width=0.5)

p3.patches('xs','ys', source=geo_source,
          fill_color={'field': 'gwad', 'transform': color_mapper},
          fill_alpha=0.7, line_color='black', line_width=0.5)
hover = HoverTool(tooltips=[('District', '@NAME_2'), ('Yield', '@gwad')])
p3.add_tools(hover)


color_bar = ColorBar(color_mapper=color_mapper, label_standoff=8, width=20, height=300,
                     border_line_color=None, location=(0,0), orientation='vertical')
p3.add_layout(color_bar, 'right')

# Plotting the fourth map
p4 = figure(title='2021 OND season yield (MT/Ha)', outer_width=600, outer_height=600)

color_mapper = LinearColorMapper(palette=Viridis256, low=min(merged_data['gwad']), high=max(merged_data['gwad']))

p4.multi_line('xs','ys', source=country_geo_source,line_color='black', line_width=0.5)

p4.patches('xs','ys', source=geo_source,
          fill_color={'field': 'gwad', 'transform': color_mapper},
          fill_alpha=0.7, line_color='black', line_width=0.5)


hover = HoverTool(tooltips=[('District', '@NAME_2'), ('Yield', '@gwad')])
p4.add_tools(hover)


color_bar = ColorBar(color_mapper=color_mapper, label_standoff=8, width=20, height=300,
                     border_line_color=None, location=(0,0), orientation='vertical')
p4.add_layout(color_bar, 'right')

# Displaying all maps under one view
p=gridplot([[p1, p2],[p3,p4]])
show(p)

