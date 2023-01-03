# import requests
# import csv
# import fonctions

# # On stocke ici tous les tokens nécessaires aux utilisation de nos différentes APIs

# # Token API Météo Concept : uniquement pour communes françaises, 500 requêtes par jour possible (plus utilisée)
# tokensLocal = {
#     "Authorization": "Bearer 06f5e42f637d611450a6004cf98f9c10b5709bac60edc77462f4a7d69e6528fc"
# }

# # Token API World Weather Online (WWO): marche pour toutes les villes du monde, 500 requêtes par jour possible 
# tokensWorld = {
#     "Authorization": "Bearer dbda99e0d09d4f9999d170804222812"
# }

# # Exemple d'appel de l'API Météo Concept
# #response_api_meteo_local = requests.get("https://api.meteo-concept.com/api/forecast/daily?latlng=48.086%2C-2.635&insee=35238&world=true&start=0&end=3", headers = tokensLocal)

# # Exemple d'appel de l'API World Weather Online
# #response_api_meteo_world = requests.get("http://api.worldweatheronline.com/premium/v1/weather.ashx?key=dbda99e0d09d4f9999d170804222812&q=48.834,2.394&format=json")

# # Parcours du dataset des villes pour récupérer toutes les longitudes et latitudes et effectuer derrière les requêtes via API World Weather Online
# # On ouvre notre dataset (sous format .csv) en mode lecture 
# with open('worldcities.csv', 'r') as Dataset_Villes:

#     # On ouvre également un csv vide pour écrire dedans toutes les valeurs récupérées de l'API afin de ne pas prendre 3h à l'éxécution du dashboard
#     with open('avg_min_temp_world.csv', 'w', newline = "") as testeur:
  
#         # On définit un reader du dataset
#         reader_Dataset_Villes = csv.reader(Dataset_Villes)

#         # On définit un writer du csv vide
#         writer_testeur = csv.writer(testeur)

#         # On créé un compteur pour tester uniquement les n premières valeurs du dataset (sinon trop d'appels pour une API gratuite)
#         cpt_appels = 0
#         # On définit un nombre limites d'appels 
#         N = 41000

#         # On parcourt chaque ligne du dataset
#         for row_Dataset_Villes in reader_Dataset_Villes:
#             try :
#                 # On extrait du dataset le nom et les coordonnées GPS (latitude, longitude) de la ville 
#                 city_name = row_Dataset_Villes[1].split(',')
#                 city_latitude = row_Dataset_Villes[2].split(',')
#                 city_longitude = row_Dataset_Villes[3].split(',')
#                 #print(city_latitude[0])

#                 # On accède au premier élément de chaque liste et les convertit en chaîne de caractères
#                 city_latitude = str(city_latitude[0])
#                 city_longitude = str(city_longitude[0])

#                 # On construit l'url d'une requête API World Weather Online pour chaque ville, qui prendra en paramètre le token, ainsi que les coordonnées gps de la ville (issues du dataset)
#                 # Cette requête renverra toutes les données météorologiques de cette ville sur un an
#                 tmp_url = "https://api.worldweatheronline.com/premium/v1/weather.ashx?key=dbda99e0d09d4f9999d170804222812&q="
#                 tmp_url += (city_latitude + "," + city_longitude + "&format=json")

#                 #print(tmp_url)

#                 # On lance la requête GET API WW0
#                 response_api_meteo_world = requests.get(tmp_url)

#                 # SI la réponse de l'API est valide (status code 200), le traitement des données peut être effectué
#                 if response_api_meteo_world.status_code == 200:

#                     # On récupère la réponse de l'API sous la forme d'un dictionnaire JSON
#                     data = response_api_meteo_world.json()
#                     #fonctions.TestPrintKeys(data)

#                     # Ce dictionnaire comporte une seul clé primaire, "data". On entre dans cette clé 
#                     data1 = data["data"]

#                     # On accède à la clé "ClimateAverages" au sein de la clé "data"
#                     climate_averages = data1["ClimateAverages"]
#                     #print(climate_averages)
                    
#                     # On accéde aux regroupement des données séparées de manière mensuelle au sein de la clé "ClimateAverages"
#                     month_list = climate_averages[0]

#                     # On accède aux données mensuelles de manière individuelle
#                     month = month_list["month"]

#                     # On initialise la variable qui contiendra la somme des températures mensuelles moyennes par ville
#                     somme_avg_min_temp_month = 0
                    
#                     # On accède aux données de chaque mois
#                     for cpt_mois in range(0,11):
#                         mois = month[cpt_mois]

#                         # On récupère la clé "avgMinTemp" de chaque mois 
#                         avg_min_temp_month = mois["avgMinTemp"]
                        
#                         # On convertit cette valeur en float (sous forme d'une string à la base) et on l'ajoute à la somme des températures mensuelles moyennes par ville
#                         somme_avg_min_temp_month += float(avg_min_temp_month)

#                     # On définit une variable qui représente la température moyenne de la ville de manière annuelle 
#                     avg_min_temp_year = somme_avg_min_temp_month / 12
#                     print("" + str(cpt_appels) + " : " + str(avg_min_temp_year)
#                     )
#                     writer_testeur.writerow([avg_min_temp_year])

#                 else:
#                     # S'il y a eu une erreur, on affiche le code de l'erreur pour avoir une idée d'où elles provient (erreur d'acccès, de requête, etc)
#                     print(response_api_meteo_world.status_code)

#                 # On incrémente le compteur d'appels à chaque tour de boucle 
#                 cpt_appels += 1
#                 # Si ce compteur dépasse N, alors on stoppe la boucle (fait pour limiter les requêtes car API WWO limite à 500 requêtes par jour)

#                 if cpt_appels >= N:
#                     break
            
#             except IndexError: 
#                 # S'il y a une IndexError, c'est que l'API ne peut pas récupérer de coordonnées à ces doordonnées. On met donc dans le fichier une valeur reconnaissable (150) afin de remplir une ligne quand même.
#                 # Il est important de remplir une ligne quand même afin de conserver le même nombre de lignes que le fichier original afin de pouvoir avoir une concordance sur chaque ligne entre la ville et sa température
#                 writer_testeur.writerow([150])
#                 print("Erreur : l'index {} est en dehors des limites de la liste".format(cpt_appels))
#                 continue

        

        



            


            





            







