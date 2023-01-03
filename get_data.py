import os
import shutil

# On liste ici tous les noms des datasets du projet à télécharger
filenames = ['countries.csv', 'worldcities.csv', 'GPS.csv', 'GPS2.csv', 'avg_min_temp_world.csv']

# On créé un répertoire 'downloads' au sein du répertoire courant si nécessaire
if not os.path.exists('downloads'):
  os.makedirs('downloads')

# On copie chaque fichier du répertoire courant dans le répertoire 'downloads'
for filename in filenames:
  shutil.copy(filename, 'downloads')