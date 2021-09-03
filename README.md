# VolcanoMap

The code produces a map showing volcanoes in USA, and shows name and height when clicked. 
Volcanoes colour coded based on height:
Green < 2000
Orange 2000-3000 metres
Red >= 3000 metres

Volcanoes and world population colours can be turned on/off with layer control check box.

World population colour coded:
Green < 10 million
Orange = 10-20 million
Red > 10 million

python libraries used: 
from branca.element import IFrame
import folium
import pandas

