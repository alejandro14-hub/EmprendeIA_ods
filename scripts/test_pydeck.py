import pydeck as pdk
import pandas as pd
df = pd.DataFrame({'lon': [-100], 'lat': [20], 'elevacion': [1000], 'color': [[255,0,0,255]], 'nombre_geo': ['Test']})
data = df.to_dict(orient="records")
layer = pdk.Layer("ColumnLayer", data=data, get_position=["lon", "lat"], get_elevation="elevacion", get_fill_color="color")
deck = pdk.Deck(layers=[layer])
print(deck.to_html(as_string=True)[:100])
