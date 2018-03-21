# Le temps de 6.892
# La distance est de 19.7 metres
# Calculer la vitesse qui est distance/temps
# Imprimer le resultat avec la fonction format de python

temps = 6.892
distance = 19.7
vitesse = distance / temps

# print("Le temps est de {0} heures, la distance est de {1} Km, la vitesse est donc de {2} Km/h.".format(temps, distance, vitesse))

val = "exercise vitesse"
print("title = {}".format(val))
print("{}".format("-"*23))
str='la vitesse est de {:.2f} km/h'
print(str.format(vitesse))