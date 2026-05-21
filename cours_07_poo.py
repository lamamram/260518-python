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
  # je fais un clone en  du compte générique
  acc = account.copy()
  acc["balance"] = balance
  acc["overdraft"] = overdraft
  return acc

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
  print(account)
  
# %% --- même exemple en Programmation Orientée Objet (POO) ---------

## REM. Classe  == Type de donnée en python
class Account:
## les classes sont nommées en PascalCase ou camelCase != snake_case

  # "variables internes" => ATTRIBUTS et en particuliuer les attributs de classe
  # ce sont les attributs de classe
  # balance = 0.
  # overdraft = 0.
  # "fonctions internes" => METHODE == ATTRIBUT de type fonction 
      # account est l'objet lui même 
      # => donc on a pas besoin de l'ajouter quand l'objet instancié appelle la méthode
      # on accède aux éléments internes avec l'opérateur "."
  # self est l'objet qu'on va créer dans le prog. principal
  # self est toujours le 1er paramètre de toute méthode
  
  def __init__(self, balance: float, overdraft: float=200) -> None:
    self.balance = balance
    self.overdraft = overdraft

  def withdraw(self, amount: float):
    if amount < 0:
      print(f"Transaction refusée: {amount} négatif")
    elif amount > self.balance + self.overdraft:
      print(f"Transaction refusée: {amount} fonds insuffisants")
    else:
      self.balance -= amount
      print(f"Transaction acceptée")
## programme principal

if __name__ == "__main__":
  ## REM. on peut appeler une classe et retourner une variable de type Account 
  ## => le terme exact est instancier (créer) un objet de cette classe
  # 1. créer un objet account à partir de l'instanciation de la classe()
  # 2. donner 1000 au solde de l'objet account et 200 au découvert d'account
  
  ## instanciation sans __init__ avec les attributs de classes 
  ## qui deviennent des attributs d'objet
  # personal_account = Account()
  # personal_account.balance = 1000
  # personal_account.overdraft = 200
  # print(f"balance de la classe: {Account.balance}")
  # print(f"balance de l'objet: {personal_account.balance}")
  # personal_account = Account(balance=1000, overdraft=200)

  ## instanciation avec __init__
  # pas besoin d'attributs de classes cat les attributs d'objet sont créés au moment
  # de la création de l'objet
  personal_account = Account(1000)

  # 3. faire un retrait
  personal_account.withdraw(100)
  print(f"nouveau solde: { personal_account.balance }")


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
d

class Truc:
  pass

t = Truc()

# afficher le type de t et de d
type(d), type(t)
# vérifier que t est d'instance de Truc  et d instance de dict avec isinstance()
isinstance(d, dict), isinstance(t, Truc)

# %% ------------------------ exemple client ---------------------------------

# créer une classe client qui contient firstname, name, et date_joint
# et 2 méthodes: 
#     get_full_name: retourne le prénom capitalisé et le nom en majuscule
#     get_date_joint: retourne la date dans le format voulu en paramètre



# %% -------------------------- héritage simple -----------------------------

# reprendre l'exemple précédent sachant qu'un client EST une personne avec un prénom et un nom
## person est considérée comme classe parente de client
## client est //                      enfant de personne , hérite de personne
from datetime import datetime

class Person:
  def __init__(self, f: str, l: str):
    self.firstname = f
    self.lastname = l
  
  def get_fullname(self) -> str:
    return f"{self.firstname.capitalize()} {self.lastname.upper()}"
## la classe enfant peut réutiliser directement les méthodes parentes
## la classe enfant peut également créer ses propres méthodes
## super().<methode>() permet d'exécuter une méthode de la classe PARENT 
## dans la classe ENFANT et sur l'objet ENFANT

# classe personne
#    utilise prénom et nom

# classe client est une personne
#    utilise prénom, nom et date_joint      
class Client(Person):
  def __init__(self, firstname: str, lastname: str, date_str: str, date_format: str="%Y-%m-%d"):
    super().__init__(firstname, lastname)
    self.date_joint = datetime.strptime(date_str, date_format)

  def get_date_joint(self, format: str="%Y-%m-%d") -> str:
    return self.date_joint.strftime(format)


cl = Client("john", "doe", "2016-05-21")
cl.get_fullname()
# %% ------------------------- injection de dépendances -----------------------------

# relation de type AVOIR entre une classe "utilisateur" et une autre qui est une dépendance
# l'utilisateur mange sa dépendance à l'instanciation et utilise LA SIGNATURE PUBLIQUE de cette dépendance


# %% ------------------------- héritage multiple + polymorphisme --------------------


# %% ------------------------ méthodes magiques ------------------------


# %% -------------- itérateur / itérable ---------------



# %% ------------------------- gestionnaire de contexte --------------------


# %%
