#faire un import de sys
#mettre sys.version_info dans une variable
#afficher le resultat dans une chaine de caracteres
#attention a utiliser str() et les acces par un tableau d'indices dans une liste

import sys

version = sys.version_info

print(version)

versionTab = str(version[0])+"."+ str(version[1])+"."+str(version[2])+"."+str(version[3])+"."+str(version[4])
print("Hello Python (version "+ versionTab+")")

version = ".".join(str(x) for x in version)
print("Hello Python (version "+ version + ")")
