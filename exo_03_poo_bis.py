"""
1/ créer un package "bank" dans le sous dossier workdir
2/ créer un module "misc.py" dans le package
3/ dans misc.py, copier la classe Account
4/ créer une classe Client qui contient
   - 3 attributs: un prénom, un nom, un objet date qui représente la date d'inscription
   - l'initialisation des objets utilise 4 attributs
     + prénom, nom, une date en str et un format de date
   - une méthode qui retourne le nom complet du client avec des majuscules
5/ ???
6/ tester le programme principal dans ce module courant
"""

# %%

from bank.misc import Account, Client

acc = Account(1000)
print(acc.balance)

cl = Client("john", "doe", "2025-05-21")
print(cl.get_fullname())
# %%
