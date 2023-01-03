import plotly.express as px
import pandas as pd
import avg_min_temp_world

# On récupère la liste de données des températures moyennes minimales par an par ville
data_avg_min_temp_year = avg_min_temp_world.read_avg_min_temp_year_world()
data_avg_min_temp_year = sorted(data_avg_min_temp_year)

# On définit 12 compteurs pour notre piechart, chacun correspondant à une tranche en particulier 
A = 0
B = 0
C = 0
D = 0
E = 0
F = 0
G = 0
H = 0
I = 0
J = 0

# On parcourt chacune des lignes de la liste et on incrémente le bon compteur selon la valeur de la température lue
for row in data_avg_min_temp_year:
    if float(row) <= -15:
        A += 1
    elif float(row) >= -15 and float(row) <= -10:
        B += 1
    elif float(row) >= -10 and float(row) <= -5:
        C += 1
    elif float(row) >= -5 and float(row) <= 0:
        D += 1
    elif float(row) >= 0 and float(row) <= 5:
        E += 1
    elif float(row) >= 5 and float(row) <= 10:
        F += 1
    elif float(row) >= 10 and float(row) <= 15:
        G += 1
    elif float(row) >= 15 and float(row) <= 20:
        H += 1
    elif float(row) >= 20 and float(row) <= 25:
        I += 1
    elif float(row) >= 25:
        J += 1

print("A = " + str(A))
print("B = " + str(B))
print("C = " + str(C))
print("D = " + str(D))
print("E = " + str(E))
print("F = " + str(F))
print("G = " + str(G))
print("H = " + str(H))
print("I = " + str(I))
print("J = " + str(J))

# On définit les différents compteurs comme les différentes valeurs du piechart, et on nomme les labels correspondants
values = [A, B, C, D, E, F, G, H, I, J]
labels = ['Inférieures ou égales à -15 °C', '-15°C - -10°C', '-10°C - -5°C', '-5°C - 0°C', '0°C - 5°C', '5°C - 10°C','10°C - 15°C', '15°C - 20°C', '20°C - 25°C','Supérieures ou égales à 25°C']
 

# On créé le piechart et on lui ajoute un titre
fig = px.pie(values=values, names=labels)
fig.update_layout(title = "Répartition des températures à la surface terrestre (hors zone océanique)")

# On définit une fonction permettant de renvoyer la figure
def return_piechart():
    return fig

