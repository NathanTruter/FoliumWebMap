import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
pop = pandas.read_csv
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def color(elevation):
    if elevation < 2000:
        return "green"
    elif elevation < 3000:
        return "orange"
    else:
        return "red"

map = folium.Map(location=[36,-115], zoom_start=5, tiles="Stamen Terrain")
fgv = folium.FeatureGroup(name="Volcanoes Western America")
fgp = folium.FeatureGroup(name="Population")

for lt, ln, lv in zip(lat, lon, elev):
    fgv.add_child(folium.Marker(location=[lt,ln],popup=str(lv)+" m", icon=folium.Icon(color=color(lv))))

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 50000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Map1.html")
