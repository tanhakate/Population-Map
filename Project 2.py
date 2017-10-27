import folium
import pandas


lat = [39.95,27.04,18.52,37.77, 24]
lon = [-86.13,88.26,73.86,-122.42,90]
purpose = ['Exchange Program, 2014', 'Boarding School, 2007','Summer School, 2016','College, 2017','Born']

map = folium.Map(location=[24,90], zoom_start= 6, tiles="Mapbox Bright")
fg = folium.FeatureGroup(name="My Map")

for lt,ln,purp in zip(lat,lon,purpose):
    fg.add_child(folium.Marker(location = (lt,ln), popup = str(purp), icon=folium.Icon(color='lightgray')))


fgp = folium.FeatureGroup(name='Population')

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fg)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("Map.html")
