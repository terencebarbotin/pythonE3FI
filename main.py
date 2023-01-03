import dash
from dash import dcc
from dash import html
from dash.dependencies import Output, Input

import plotly.graph_objects as go
import plotly.express as px
import plotly.graph_objects as go

import data
import avg_min_temp_world
import carte_monde
import piechart

import pandas as pd 
import geopandas as gpd

import numpy as np
import importlib

# On récupère la liste comportant les températures minimales par ville par an : 
data_avg_min_temp_year = avg_min_temp_world.read_avg_min_temp_year_world()
# On trie cette liste pour les avoir de manière croissante plus tard dans l'histogramme
data_avg_min_temp_year = sorted(data_avg_min_temp_year)

# On créé l'application dash
app = dash.Dash()

# On créé le layout de l'application avec le titre, le contexte, ainsi que nos 3 graphiques à la suite
app.layout = html.Div(children = [
    # On créé le titre de notre application
    html.H1(children = 'Croissance de la température dans le monde :', style = {'text-align': 'center', 'text-shadow' :'0 0 2px #00FFFC,0 0 30px #00FFFC,0px 0px 5px #00FFFC, 0 0 150px #00FFFC', 'color':'#00FFFC','background-color': '#2E8ECE'
    }),
    # On créé un paragraphe, le contexte de notre application
    html.Div(children = '''
        Projet Python E3FI : Eclairer un sujet d’intérêt public en utilisant des données Open Data, accessibles, et non modifiées.
    ''', style = {'text-align' : 'center'}),
    # On créé la map monde montrant la température de chaque pays en temps réel
    dcc.Graph(
        id = 'worldmap', figure = carte_monde.return_carte_monde()
    ),
    # On créé le pie chart montrant la répartition des températures moyennes minimales à la surface terrestre ces douze derniers mois
    dcc.Graph(
        id = 'piechart', figure = piechart.return_piechart()
    ),
    # On créé l'histogramme des températures moyennes minimales à la surface terrestre ces douze derniers mois
    dcc.Graph(
        id = 'histogram-graph'
    ),
    dcc.Input(id = "data", type = "number")
])

# On définit à l'aide de cette formule le meilleur nombre de bins, adapté à notre nombre de données pour l'histogramme (environ 40K ici)
bins =  int(np.sqrt(len(data_avg_min_temp_year)))

# On définit une fonction permettant l'update de l'histogramme 
def update_histogram(data):

    # On créé l'histogramme à l'aide de notre liste créée plutôt ainsi que du nombre de bins optimal 
    fig = px.histogram(x = data_avg_min_temp_year, nbins = bins)

    # On définit le titre du graphique, ainsi que le nom de ses axes 
    fig.update_layout(title="Histogramme des températures moyennes minimales à la surfacce terrestre (hors zone océanique)", titlefont={"size": 20, "family": "Arial"})    
    fig.update_xaxes(title="Température moyenne minimale")
    fig.update_yaxes(title="Compteur")
    return fig

# On définit le callback de l'update de l'histogramme
@app.callback(Output("histogram-graph", "figure"), [Input("data", "value")])
def update_histogram_callback(data_avg_min_temp_year):
    fig = update_histogram(data)
    return fig

# On saute une ligne pour marquer le lancement de l'application, puis on lance l'application
if __name__ == '__main__':
    print()
    app.run_server(debug=True)
