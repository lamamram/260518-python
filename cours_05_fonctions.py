# %% ---------- définition et appel d'une fonction -----------------------
### une fonction est un objet créé/définie avec: 
### le mot clé def suivi de <nom_de_la_fonction>(): 
###     et après un bloc d'instructions  

# définition d'une fonction ma_fonction() qui contient l'affichage de "coucou"
def ma_fonction():
    print("coucou")

### pour exécuter le bloc de la définition, on doit appeler la fonction 
### <nom_de_la_fonction>()
### (): opérateur d'appel
### une fonction est un type de donnée dite "callable"

# afficher l'appel de la fonction ma_fonction
print("appel de ma_fonction => ", ma_fonction())
# %% ----------- retour d'une fonction ------------------------------

# même définition mais en remplaçant le print("coucou") par le mot clé return et 'coucou'
def ma_fonction():
  return "coucou"

# afficher l'appel de la fonction
print("appel de ma_fonction() => ", ma_fonction())
# alternativement, on peut affecter l'appel de la fonction dans une variable
ret = ma_fonction()
# %% -- définition d'une fonction avec des paramètres et appel des paramètres ---

# définir une fonction qui ajoute 2 entiers en paramètres et qui retourne la somme 
# a, b dans la définition de la focntions sont des paramètres formels
def addition(a, b):
    return a + b

# injection des variables globales en tant que paramètres d'appel: passage en référence
addition(2, 3)
# print(f"appel de addition("ff", "rr") => ", addition("ff", "tt")) ERROR
addition("ab", "cd")

# addition(2, "ab")
# %% ------------ annotations, documentation et contrôle -------------------


# créer une fonction division de 2 floats qui retourne un float
# les annotations ne sont pas des contrôles, ce ne sont que des indications
def division(a: float, b: float) -> float :
    """
    fonction de division de réels blablab
    """
    # if b == 0:
    #     return "zéro par division"
    return a/b

# 1. en notifiant les types d'entrée et de sortie de la fonction
# 2. documenter la fonction en ajoutant une """doctstring""" au début du bloc
division(5, 2)
# 3. faire un contrôle sur le dénominateur
division(5, 0)
# sans rien => çà plante il faut rajouter une gestion d'exception
# on peut gérer l'erreur dans la fonction donc le programme principal devra gérer le retour spécial
# %% --------------- passage en référence de types mutables et immutables ------------------

# def immutable(x: int):
#       x += 1
#       print("x: local", x, id(x))
#       return x

# x = 5
# print("global avant appel", x, id(x))
# x = immutable(x)
# print("global après réaffectation", x, id(x)) # x global prend l'id du x local

def mutable(l: list, elem: int):
      l.append(elem)
      print(l, id(l))

l = [1, 2, 3]
print(f"avant appel de mutable: {l}, {id(l)}")
mutable(l, 4)
print(l, id(l)) # l global a changé car l est mutable => le l local

# %% --------------- types de paramètres ----------------------------------

# créer une fonction calcul_tva qui prend 2 paramètres le prix ht et le taux
# et retourne la valeur de tva sur ce prix et ce taux
# 1. annotations et documentation
# 2. le prix est arbitraire => paramètre positionnel / obligatoire
# MAIS on considère que la valeur par défaut du taux est 20 => paramètre nommé / optionnel
def calcul_tva(price: float, vat_rate: float=20) -> float:
    """ partie liée à la tva dans un prix ttc"""
    return price * vat_rate / 100
# appeler la fonction sans paramètres

print(f"""appel positionnel: 199 -> prix_ht, 5.5 -> taux 
       => {calcul_tva(199, 5.5)} """)
print(f"""appel avec un paramètre optionnel: 199 -> prix ht et rien -> taux
       => {calcul_tva(199)} """)
print(f"""appel nommé: les valeurs sont fléchées vers les paramètres 
       => pas besoin d'ordre => {calcul_tva(vat_rate=5.5, price=199)} """)

# %% ---------------- paramètres "variadiques" *args ---------------------
## *args: permet de définir un nombre variable de paramètres positionnels
## le bloc peut alors utiliser un tuple args

# exemple: print
# on veut afficher tous les mots soudés par "-" à partir de 2 prints
# et les 2 paramètres nommées "sep" et "end"

print("bonjour", "tout", "le", "monde", sep="-", end="-")
print("comment", "allez", "vous", sep="-")


# créer une fonction addition qui peut ajouter un nombre quelconque de params
def addition(*nbs):
    # nbs est un tuple
    return sum(nbs)

addition(1, 2, 3)
addition(1, 5, 7, 9)

# %% -------------- *args dans l'appel -------------

def ma_fonction(a, b, c):
    return a, b, c

l = [1, 2, 3]
# injecter les éléments de la liste l en tant que paramètres d'appel de ma_fonction

# %% paramètres "variadiques" **kwargs
## **kwargs: permet de définir un nombre variable de paramètres nommés
## le bloc peut alors utiliser un dict kwargs

# créer une fonction create_user avec
def create_user(firstname, lastname, **options):
    user = {
        "firstname": firstname,
        "lastname": lastname
    }
    for k, v in options.items():
      user[k] = v
    return user
# 1. le prénom et le nom obligatoires
# 2. et un nombre quelconque de paramètres nommés/optionnels
# 3. pour créer et retourner un dictionnaire user 
#    avec les paramètres obligatoires et les autres s'ils existent (age, taille...)
print(create_user("john", "doe"))
print(create_user("john", "doe", age=20, taille=1.75))

# %% ------------ **kwargs dans l'appel -------------

def ma_fonction(a, b, c):
    return a, b, c

dico = {"a": 1, "b": 2, "c": 3}
# inejcter les valeurs du dict dico en tant que paramètres nommés d'appel de ma_fonction




# %%
