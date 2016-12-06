#!/usr/bin/python

import folium
import pandas

mymap = folium.Map(
    location=[45.372, -121.697],
    zoom_start=4,
    tiles='Stamen Terrain')

df = pandas.read_csv("Volcanoes-USA.txt")

for lat, lon, name in zip(df['LAT'], df['LON'], df['NAME']):
    mymap.simple_marker(
        location = [lat, lon],
        popup = name,
        marker_color = 'red')

mymap.create_map(path="test2.html")
