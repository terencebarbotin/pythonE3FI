# On ouvre le fichier csv avec les données non formatées en mode lecture
with open('GPS.csv', 'r') as fichier_csv:

  # On ouvre un nouveau fichier vide en mode écriture
  with open('GPS2.csv', 'w') as nouveau_fichier:

    # On parcoure chaque ligne du fichier csv
    for ligne in fichier_csv:
      # On enlève tous les caractères non nécessaires de chaque ligne
      ligne_modifiee = ligne.replace(',', '').replace('"', '').replace('[', '').replace(']', '').replace("'", '').replace(' ', ', ').replace('(', '').replace(')', '')
      
      # On écrit la ligne modifiée dans le nouveau fichier
      nouveau_fichier.write(ligne_modifiee)
