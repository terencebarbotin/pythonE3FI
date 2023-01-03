import plotly.express as px
import pandas as pd
import geopandas as gpd
import dash
from dash import dcc
from dash import html
from dash.dependencies import Output, Input
import glob
import importlib
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import data
import csv

# On ouvre notre fichier csv
with open('worldcities.csv', 'r') as Dataset_Villes:

    # On ouvre un autre fichier csv vide en tant qu'éditeur
    with open('GPS.csv', 'w', newline = "") as Dataset_GPS:

        reader_Dataset_Villes = csv.reader(Dataset_Villes)

        writer_Dataset_GPS = csv.writer(Dataset_GPS)

        # On créé un compteur pour tester uniquement les n premières valeurs du dataset (sinon trop d'appels pour une API gratuite)
        cpt_appels = 0
        # On définit un nombre limites d'appels 
        N = 41000

        for row_Dataset_Villes in reader_Dataset_Villes:
                try:
                    
                    # On extrait du dataset le nom et les coordonnées GPS (latitude, longitude) de la ville 
                    city_name = row_Dataset_Villes[1].split(',')
                    city_latitude = row_Dataset_Villes[2].split(',')
                    city_longitude = row_Dataset_Villes[3].split(',')

                    # On écrit à chaque itération les coordonnées uniquement de la ville dans le nouveau fichier csv
                    writer_Dataset_GPS.writerow("(" + str(city_latitude) + ", " + str(city_longitude) + ")")

                    print(str(cpt_appels) + "(" + str(city_latitude) + ", " + str(city_longitude) + ")")

                    # On incrémente le compteur d'appels à chaque tour de boucle 
                    cpt_appels += 1
                    # Si ce compteur dépasse N, alors on stoppe la boucle (fait pour limiter les requêtes car API WWO limite à 500 requêtes par jour)

                    if cpt_appels >= N:
                        break

                except IndexError:
                    print("Erreur : l'index {} est en dehors des limites de la liste".format(cpt_appels))

    

