import dash
from dash import dcc

from dash import html

from dash.dependencies import Output, Input


import glob
import importlib

import plotly.graph_objects as go
import plotly.express as px

import data

# # On récupère la liste de tous les fichiers Python du répertoire dash-recipes-master 
# python_files = glob.glob("dash-reciped-master/*.py")

# # On parcourt chacun des fichiers du répertoire
# for file in python_files:

#     # On en extrait le nom du fichier (sans le répertoire ou l'extension)
#     file_name = file.split("/")[-1][:-3]

#     # On importe le fichier Python en tant que module
#     importlib.import_module(file_name)

# On récupère le fichier comportant les températures minimales par ville par an : 
data_avg_min_temp_year = data.calcul_avg_min_temp_year()


# On créé l'application dash
app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children='Croissance de la température dans le monde :', style={'text-align': 'center'}),

    html.Div(children='''
        Projet Python E3FI : Eclairer un sujet d’intérêt public en utilisant des données Open Data, accessibles, et non modifiées.
    '''),

    # dcc.Graph(
    #     id='example-graph',
    #     figure={
    #         'data': [
    #             {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
    #             {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
    #         ],
    #         'layout': {
    #             'title': 'Données de test'
    #         }
    #     }
        
    # ),
    # dcc.Graph(
    #     id='example-graph2',
    #     figure={
    #         'data': [
    #             {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
    #             {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
    #         ],
    #         'layout': {
    #             'title': 'Données de test'
    #         }
    #     }
    # ),
    dcc.Graph(
        id='histogram-graph'
    ),
    dcc.Input(id="data", type="value")
])

def update_histogram(data):
    fig = px.histogram(x=data_avg_min_temp_year, nbins=50)
    return fig


@app.callback(Output("histogram-graph", "figure"), [Input("data", "value")])
def update_histogram_callback(data_avg_min_temp_year):
    fig = update_histogram(data_avg_min_temp_year)
    return fig

if __name__ == '__main__':
    print()
    app.run_server(debug=True)
    print("test")


    