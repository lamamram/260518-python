# %% un exemple en programmation impérative / procédurale 
# sans programmation orientée objet

## initialisations

# ce dictionnaire représente la strucutre générique d'un compte
account = {
  "balance": 0,
  "overdraft": 0,
}

# créer une fonction init_account qui va mettre à jour les champs d'un dict account en param
# à partir de paramètres balance et overdraft
def init_account(account: dict, balance: float, overdraft: float) -> dict:
  account["balance"] = balance
  account["overdraft"] = overdraft
  return account

# créer une fonction withdraw pour effectuer un retrait d'un montant sur un compte en param.
def withdraw(account: dict, amount: float):
  if amount < 0:
    print(f"Transaction refusée: {amount} négatif")
  elif amount > account["balance"] + account["overdraft"]:
    print(f"Transaction refusée: {amount} fonds insuffisants")
  else:
    account["balance"] -= amount
    print(f"Transaction acceptée")

## programme principal
if __name__ == "__main__":
  # initialiser le dictionnaire account avec un solde de 1000 et un découvert de 200
  personal_account = init_account(account, balance=1000, overdraft=200)
  # saisir un montant, effectuer le retrait et afficher le solde après
  amount = input("Entrez un montant : ")
  amount = int(amount)

  withdraw(personal_account, amount)
  print(f"nouveau solde: {personal_account["balance"]}")
  
# %% --- même exemple en Programmation Orientée Objet (POO) ---------

## REM. Classe  == Type de donnée en python
## les classes sont nommées en PascalCase ou camelCase != snake_case

    # "variables internes" => ATTRIBUTS et en particuliuer les attributs de classe

    # "fonctions internes" => METHODE == ATTRIBUT de type fonction 
       # account est l'objet lui même 
       # => donc on a pas besoin de l'ajouter quand l'objet instancié appelle la méthode
       # on accède aux éléments internes avec l'opérateur "."

## programme principal

if __name__ == "__main__":
  pass
  ## REM. on peut appeler une classe et retourner une variable de type Account 
  ## => le terme exact est instancier (créer) un objet de cette classe
  # 1. créer un objet account à partir de l'instanciation de la classe()

  # 2. donner 1000 au solde de l'objet account et 200 au découvert d'account

  # 3. faire un retrait


# %% --------------------- utilisation de la méthode magique __init__() ------------

    # en utilisant __init__ on a pas forcément besoin d'attributs de classe
    # balance: float = 0
    # overdraft: float = 0
 
    # self est l'objet lui même
    # un attribut/méthode de forme __xxxx__ est un attribut/méthode MAGIQUE 
    # def init_account(self, balance: float, overdraft: float) -> dict:

      # ici ce sont des attributs d'objets

      # return self: pas besoin car l'objet est DEJA CREE !!!



## programme principal


# %% ------------------ encapsulation frauduleuse en python ------------------

##### MORALE DE L'HISTOIRE ##################

# il n'ya pas en réalité d'attributs privés => pas d'encapsulation effective
# par contre, on peut l'utiliser pour STRUCTURER VOS CLASSES
# protected en python c'est _var => public mais n'est pas spécifié dans la documentation

# %% ------------- en python: TOUT EST OBJET ---------------------
# instancier un objet t d'une classe Truc vide

d = dict(k1=1, k2=2)

# afficher le type de t et de d
# vérifier que t est d'instance de Truc  et d instance de dict avec isinstance()


# %% ------------------------ exemple client ---------------------------------

# créer une classe client qui contient firstname, name, et date_joint
# et 2 méthodes: 
#     get_full_name: retourne le prénom capitalisé et le nom en majuscule
#     get_date_joint: retourne la date dans le format voulu en paramètre



# %% -------------------------- héritage simple -----------------------------

# reprendre l'exemple précédent sachant qu'un client EST une personne avec un prénom et un nom
## person est considérée comme classe parente de client
## client est //                      enfant de personne , hérite de personne

## la classe enfant peut réutiliser directement les méthodes parentes
## la classe enfant peut également créer ses propres méthodes
## super().<methode>() permet d'exécuter une méthode de la classe PARENT 
## dans la classe ENFANT et sur l'objet ENFANT

# classe personne
#    utilise prénom et nom

# classe client est une personne
#    utilise prénom, nom et date_joint      


# %% ------------------------- injection de dépendances -----------------------------

# relation de type AVOIR entre une classe "utilisateur" et une autre qui est une dépendance
# l'utilisateur mange sa dépendance à l'instanciation et utilise LA SIGNATURE PUBLIQUE de cette dépendance


# %% ------------------------- héritage multiple + polymorphisme --------------------


# %% ------------------------ méthodes magiques ------------------------


# %% -------------- itérateur / itérable ---------------



# %% ------------------------- gestionnaire de contexte --------------------


# %%
