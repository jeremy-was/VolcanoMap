from branca.element import IFrame
import folium
import pandas

data = pandas.read_csv('volcanoes.txt')
lat = list(data['LAT'])
lon = list(data['LON'])
elev = list(data['ELEV'])
name = list(data['NAME'])

html = """<h4>%s</h4>
Height: %s m
"""

def colour_func(elevation):
    if elevation >= 3000:
        return 'red'
    elif elevation >= 2000 and elevation < 3000:
        return 'orange'
    else:
        return 'green'

map = folium.Map(location=[40.914841690105696, -117.88378668687105], zoom_start=5)#, tiles='Stamen Terrain')

fgv = folium.FeatureGroup(name='Volcanoes')

for lt, ln, el, nm in zip(lat, lon, elev, name):
    iframe = folium.IFrame(html=html % (nm, int(el)), width=200, height=100)
    fgv.add_child(folium.CircleMarker(location=[lt, ln], popup=folium.Popup(iframe), radius=10, fill_color=colour_func(el), color='grey', fill_opacity=0.7))
    # fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon=folium.Icon(icon='circle', color = colour_func(el))))
    # fg.add_child(folium.Marker(location=[lt, ln], popup=f'{nm}\n{int(el):,}m', icon=folium.Icon(color = colour_func(el))))

fgp = folium.FeatureGroup(name='Population')

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 
else 'orange ' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save('map1.html') 



'''
import folium

map = folium.Map(location = [54.68531, 25.28708])#, tiles = 'Stamen Terrain')

fg = folium.FeatureGroup(name = 'My Map')
fg.add_child(folium.Marker(location = [54.75531399298113, 25.252691167263844], popup = 'Muk Apartment', icon = folium.Icon(color = 'green')))
map.add_child(fg)

map.save('map1.html') 
'''