import re

st = '/usr/home:lumberjack'
match = re.match(r'\/(.*)\/(.*):(.*)', st)
print(match.groups())
print(match.groups()[0])

# creer une liste vide   mylist = []
# for une boucle for de range(5)
# entrer des valeurs au clavier avec la fonction input()
# attention a convertir les donnees en entier
# faire un tri
# afficher la liste

mylist = []
mylist2 = []

for i in range(5):
    mylist.append(int(input('Entrer un numéro : ')))



mylist.sort()

print(mylist)

[mylist2.append(int(input('Entrer un numéro : '))) for i in range(5)]


mylist2.sort()

print(mylist2)