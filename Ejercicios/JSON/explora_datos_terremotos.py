import json

# Explora la estuctura de datos.
nombreFichero = 'datos/eq_data_1_day_m1.json'
with open(nombreFichero) as f:
    todos_los_datos = json.load(f)

todos_los_diccionarios = todos_los_datos['features']

magnitudes, longitudes, latitudes = [], [], []
for diccTerremotos in todos_los_diccionarios:
    magnitudes = diccTerremotos['properties']['mag']
    longitudes = diccTerremotos['geometry']['coordinates'][0]
    latitudes = diccTerremotos['geometry']['coordinates'][1]
    magnitudes.append(mag)
    longitudes.append(lon)
    latitudes.append(lat)

print(magnitudes[:10])
#print(longitudes[:5])
#print(latitudes[:5])
