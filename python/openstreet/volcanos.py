#!/usr/bin/python

import folium
import pandas

df = pandas.read_csv("Volcanoes-USA.txt")

mymap = folium.Map(
    location=[df["LAT"].mean(), df["LON"].mean()],
    zoom_start=4,
    tiles='Stamen Terrain')

# Rango 1
# menor valor ... (menor valor + (valor maximo - valor menor)) / 3
# Rango 2
#


def color(elev):

    minimum = int(min(df["ELEV"]))
    step = int((max(df["ELEV"]) - min(df["ELEV"])) / 3)

    if elev in range(minimum, minimum + step):
        col = 'blue'
    elif elev in range(minimum + step, minimum + step * 2):
        col = 'green'
    else:
        col = 'orange'
    return col


for lat, lon, name, elev in zip(df['LAT'], df['LON'], df['NAME'], df['ELEV']):

    #if elev > 3000:
        #color = 'red'
    #elif elev >= 1000 or elev <= 3000:
        #color = 'orange'
    #elif elev < 1000:
        #color = 'yellow'
    #else:
        #color = 'blue'

    mymap.add_children(folium.Marker(
            location=[lat, lon],
            popup=name,
            icon=folium.Icon(color=color(elev))))

mymap.save(outfile="test4.html")
