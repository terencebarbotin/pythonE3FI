import pandas as pd
import requests
import plotly.express as px
import json

# On lit à l'aide de pandas le fichier csv contennant tous nos pays ainsi que leur localisation
countries = pd.read_csv("countries.csv")

# On ouvre notre fichier geojson permettant de faire les contours de notre map
with open('countries.geojson') as count:
    countries_json = json.load(count)

# On note ici la clé de notre API Météo (différente de celle utilisée dans data.py)
api_key = "1a519ffe84f8e0c08ae2b23d41546fd6"

# On définit les coordonnées de chacun de nos pays contenu dans le fichier csv
countries = countries.dropna()
countries = countries[countries['latitude'].astype(str) != '']
countries = countries[countries['longitude'].astype(str) != '']

# On parcourt chacune des lignes de notre fichier
for index, row in countries.iterrows():

        # On définit une latitude et longitude pour chacun des pays
        lat = str(row["latitude"])
        lon = str(row["longitude"])
    
        # On créé pour chaque pays une URL de requête à l'API
        api_uri = "https://api.openweathermap.org/data/2.5/weather?lat="+lat+"&lon="+lon+"&appid="+api_key

        # On effectue cette requête 
        response = requests.get(api_uri)

        # On la onvertit en json
        response_json = response.json()
        
        # On en extrait la température et on la convertit en celsius
        temp = response_json["main"]["temp"] - 273.15
        countries.loc[index, 'temp'] = temp

        # On print pour savoir où on en est dans le traitement des requêtes (compter environ 2 minutes max pour tout traiter)
        print(index, row["name"])
    

# On créé la map
fig = px.choropleth_mapbox(
    data_frame = countries,
    geojson = countries_json,
    featureidkey="properties.ISO_A2",
    locations = "country",
    color_continuous_scale="thermal",
    mapbox_style="carto-positron",
    color = "temp",
    zoom=1,
    center = {'lat':48.690236,'lon':2.498065},
    opacity = 0.5,
    title = "Températures mondiales en temps réel"
)

# On définit une fonction permettant de retourner la figure 
def return_carte_monde():
    return fig