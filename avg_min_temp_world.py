import csv

# Fonction qui renvoie la liste des tempéraures moyennes minimales par an par ville récupéré au préalabe par data.py dans un fichier csv
def read_avg_min_temp_year_world():
    # On ouvre le fichier csv en tant que lecteur 
    with open('avg_min_temp_world.csv', 'r') as Dataset_Avg_Min_Temp_year_world:

        # On définit un reader du csv
        reader_Avg_Min_Temp_year_world = csv.reader(Dataset_Avg_Min_Temp_year_world)

        # On créé une liste vide 
        data = []

        # On créé un compteur, uniquement pour se repérer à l'aide de prints
        cpt = 0

        # On parcourt chacune des lignes du csv 
        for row_Dataset_Avg_Min_Temp_Year_World in reader_Avg_Min_Temp_year_world:

            avg_min_temp_year_world = row_Dataset_Avg_Min_Temp_Year_World[0]

            # Comme défini dans data.py, pour les lignes où il était impossible de récupérer la température, nous y avons mit la valeur 150 dans le csv afin de garder un ordre de lignes adéquat avec les coordonnées GPS. IL est donc primordial de sauter ces lignes là pour ne pas fausser les données.
            if(avg_min_temp_year_world != "150"):

                # SI les valeurs dont doc différentes de 150, on ne les ajoute pas à la liste
                data.append(avg_min_temp_year_world)
                
            cpt += 1

        # On retourne la liste enfin complétée 
        return data


            

        



