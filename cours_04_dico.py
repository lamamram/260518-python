# %% ------------------- créer un dictionnaire: dict ----------------------

#       {         paire      , paire    }
#       { clé       : valeur , clé  : valeur}
user =  {"firstname": "roger", "age": 56}

## REM: les clés sont uniques et peuvent être n'importe quel type immutable
# créer un dict ayant 
# des clés de type tuple à 2 éléments qui représentent la latitude et la longitude
# et des valeurs qui sont les noms des villes liés à ces coordonnées 
cities = {
  (2.45, 43.13): "PARIS",
  (5.435, 32.13): "MARSEILLE"
}
# %% -------------- accéder à la valeur d'une clé -------------
user =  {"firstname": "roger", "age": 56}


# afficher la valeur liée à la clé 'firstname'
print(user["firstname"], cities[(2.45, 43.13)])
# afficher le nom d'une ville liée à un point


# %% --------- remplacer une valeur, créer une clé, ... --------
user =  {"firstname": "roger", "age": 56}
# remplacer le prénom
user["firstname"] = "fred"

# ajouter un email

user["email"] = "fred@example.com"

# supprimer age du dict
# user.pop("age")
del user["age"]

print(user)

# afficher la taille de user si la clé existe dans user 
# ou afficher une valeur par défaut N/A
# if "taille" in user:  # acvec les dico in fonctionne avec les clés
#   print(user["taille"])
# else:
#   print("N/A")

# idem en une seulle ligne
print(user.get("taille", "N/A"))



# %% ---------------- itérer sur un dictionnaire -----------------
user = {"firstname": "roger", "age": 56}
# par défaut on boucle un dico avec les clés
# tester si un dictionnaire est un itérable
for key in user:
  print(key)

# afficher la conversion d'un dictionnaire en liste
print(list(user))

print("-"*10 + "avec les valeurs" + "-"*10)

# afficher la liste des valeurs d'un dictionnaire

for val in user.values():
  print(val)

# itérer sur les valeurs d'un dictionnaire
print(list(user.values()))

print("-"*10 + "avec les items: clés & valeurs" + "-"*10)

# afficher la conversion d'un dictionnaire en une liste de tuples à 2 éléments
for key, val in user.items():
  print(key, val)
# itérer sur les clés & les valeurs d'un dictionnaire
print(list(user.items()))
# %% -- zip: recréer un dict à partir d'une liste de clés et une liste de valeurs --
user = {"firstname": "roger", "age": 56}

# créer la liste des clés
keys = list(user)

# créer la liste des valeurs
values = list(user.values())

# zipper les 2 listes
z = zip(keys, values)
print(z)
print(list(z))
z = zip(keys, values)
print(dict(z))

# convertir cet "objet" en liste
# print(list(z))
# convertir cet "objet" en dict
# warning: zip est un itérateur, une fois converti en liste, il ne peut plus être itéré

 

# %% -------------- gestion des sets -----------------

fruits = {"pomme", "poire", "banane"}

# tester si les sets sont indexables

# tester si un élément est dans un set
# ajouter un élément à un set
# supprimer un élément d'un set + erreur si l'élément n'existe pas
# supprimer un élément d'un set + ne fait rien

# tester si les sets sont itérables

# conversions entre set <-> list
# %%
