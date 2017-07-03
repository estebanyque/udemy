#!/usr/bin/python

import folium

#mymap = folium.Map(location=[45.372, -121.697], zoom_start=12)
#mymap.create_map(path="test.html")

mymap2 = folium.Map(
    location=[45.372, -121.697],
    zoom_start=12,
    tiles='Stamen Terrain')

mymap2.simple_marker(
    location=[45.3288, -121.6625],
    popup='Mt. Hood Meadows',
    marker_color='red')

mymap2.simple_marker(
    location=[45.3311, -121.7311],
    popup='Timberlake Lodge',
    marker_color='green')

mymap2.create_map(path="test2.html")