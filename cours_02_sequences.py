#################### séquence: str, list, tuple ############################
# %% ---------- chaines de caractères: str: concaténation ---------------

prenom = "john"
nom = "doe"

# afficher nom complet: "john doe"

# surcharge de l'opérateur + : concaténation de str
# pas de conversion implicite en python

# %% ---------- fonctions internes d'une variable selon son type : ici str ----

######### <variable>.<fonction>()

prenom = "john"
nom = "doe"

# afficher le nom complet : John DOE

# %% ------------ indéxer une séquence ------------------------------------
nom_complet = "Joe DOE"

# prendre la longueur d'une str

######## <variable>[n]: caractère de la variable à la position n 

# afficher le 1er caractère de la str, le 1er car. du 2ème mot, le dernier car.


# %% ------------- SLICING d'une séquence ----------------------------------- 

civilite_nom_complet = "Mr. Joe DOE"

######## slicing : <variable>[<index de début compris>:<index de fin non compris>]
######## slicing avec pas: <var>[deb:fin:pas]

# afficher la civilité, le prénom, le nom à partir de civilite_nom_complet

# slicing: indice de début compris: indice de fin non compris, début == 0 ou rien, fin => rien si dernier

# afficher une chaine contenant chaque 1er car. de chaque mot //

# retourner civilite_nom_complet



# %% -------------- retourner l'indice d'une str ---------------------------

civilite_nom_complet = "Mr. Joe DOe"

# afficher la civilité, le prénom, le nom à partir des indices de J et D
# 1. connaître les positions de J et D dans la chaine
index_J, index_D = civilite_nom_complet.index("J"), civilite_nom_complet.index("D")
print(index_J, index_D)
# 1. bis c'est PRESQUE l'inverse de voir le caractère à la position index_J
print(civilite_nom_complet[index_J], civilite_nom_complet[index_D])
# 1.ter: connaître la position de "e" ???
index_e1 = civilite_nom_complet.index("e")
index_e2 = civilite_nom_complet.index("e", index_e1 + 1)
print(index_e1, index_e2)

# 2. on peut "slicer" le prénom et le nom avec les indices calculés
# ------------------------ entre le J et le D (espace non compris) -------- du D vers la fin
prenom, nom = civilite_nom_complet[index_J: index_D - 1], civilite_nom_complet[index_D:]
print(prenom, nom)
# même chose mais en remettant les valeurs slicées en minuscules

# 3. j'enchaine le  slicing (qui est un str) avec son .lower
print(civilite_nom_complet[index_J: index_D - 1].lower(), civilite_nom_complet[index_D:].lower())
# en moins méchant
print(prenom.lower(), nom.lower())

# %% -------------- list: indexation, concaténation, slicing -------------

mots = ["appeler", "un", "chat"]

# afficher chat à partir de mots


# modifier mots en concaténant ["il", "faut"] , mots et ["un", "chat"]


# remettre mots dans sa valeur initiale à partir de sa valeur courante


# %% -------------- transformation de liste <=> chaîne de caractères ----------

civilite_nom_complet = "Mr. Joe DOE"

# créer la liste mots, des mots de civilite_nom_complet => split


# recréer civilite_nom_complet à partir de mots
# en soudant les élements de mots avec un " " => join


# %% ---------------- fonctions internes exclusives aux listes -----------------
mots = ["appeler", "un"]

# ajouter "chat" à droite avec [] ou autrement
# mots[2] = "chat" # [] : IndexError

mots.append("chat")
# ajouter ["chat", "un", "chat", "gris"] à droite

# ajouter "il" à gauche

# ajouter "faut" à gauche d'"appeler"


# supprimer le dernier élement de mots et retourne sa valeur

# supprimer le premier élément //

# supprimer la 1ère occurence de chat 

# %% --------------- listes et tuples / str : mutabilité et immutabilité ------------
mots = ["nommer", "un", "chien"]

# remplacer "chien" en "chat" dans mots avec []
# opération muable
mots[2] = "chat"
print(mots)

mots = tuple(mots)
print(mots)

# remplacer "nommer" en "appeler" dans mots
# mots[0] = "appeler" # TypeERROR INTERDIT avec un tuple
# transformer mots en une str phrase et mettre le 1er car. en majuscule
phrase = " ".join(mots)
print(phrase)
# phrase[0] = "N"
# opération immuable: réaffecter complètement la variable
phrase = phrase.capitalize()
print(phrase)

# %% --------------- opérateur in : test d'appartenance -----------------------

phrase = "appeler un chat"

# savoir si "chat" est dans phrase
print("chat" in phrase, phrase.count("chat"), phrase.find("chat"))

# savoir si "chien" n'est pas dans phrase
print("chien" not in phrase)

# idem en transformant phrase en mots
mots = phrase.split()
print("chat" in mots, mots.count("chat"))
# %%
