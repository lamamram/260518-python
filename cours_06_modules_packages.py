# %% ------------ import d'un module avec espace de nom ----------------

## un fichier d'extension .py avec du code python est un MODULE
## si ce module ne contient que des définitions de variables, fonctions, classes
##    ce module est une bibliothèque/librairie
## le module qui est exécuté directement par l'interpréteur python ou jupyter
##    est appelé module principal

# 1. créer un module tools qui contient la fonction de l'exercice template
import tools


# 2. importer le module est exécuter la fonction dans le module principal
# tools est une variable de type module qu'on appelle espace de nom du module

tpl = "machin: {{clef}}"
dico = {"clef": 33}
print(tools.parse_template(tpl, dico))

# %% -- à partir d'un module, importer une fonction => sans espace de nom ----
# idem sans espace de nom
from tools import parse_template as parse_tpl

# gérer les conflits de noms => alias
# idem en changeant le nom de la fonction à l'import

parse_template = "qqch d'autre"

tpl = "machin: {{clef}}"
dico = {"clef": 33}
print(parse_tpl(tpl, dico))

# %% --- exemples d'utilisation de modules de la bibliothèque standard ------
# exemple de datetime
# importer l'objet datetime à partir du module datetime

from datetime import datetime, timedelta

# créer une variable dt représente la date d'aujourd'hui avec la signature de base 

dt = datetime(2026, 5, 20, 16, 18)
dt
# idem avec une fonction interne

dt = datetime.now()
dt

# idem à partir de la chaine de caractère "2026-05-20 16:21" et le format "%Y-%m-%d %H:%M" 
dt = datetime.strptime("2026-05-20 16:21", "%Y-%m-%d %H:%M")
dt

# à partir de la variable, afficher l'année, la date au format "%d/%m/%Y", le nb de secondes à partir le 1er janvier 1970
dt.year, dt.strftime("%d/%m/%Y"), dt.timestamp()

# afficher la durée entre la fin de la journée et maintenant, en heures, min, s
delta = datetime(2026, 5, 20, 17) - datetime.now()

delta.seconds // 3600, delta.seconds % 3600 // 60, delta.seconds % 60  
# date + duree (timedelta) = date

datetime.now() + timedelta(minutes=3)
# %% ------------- import d'un module d'un package ------------------------

# ici le "." on appelle çà le "chemin python": Python Path (comme "/" ou "\")
## un package est un dossier qui contient un ou des modules ou des sous packahes 
## et qui contient un fichier nommé __init__.py qui peut être vide
import utils.tools

# utils.tools.parse_template(...)
# créer un package utils et copier le module tools dans utils
# importer tools à partir de utils

# à partir du module tools dans le package, importer la fonction
from utils.tools import parse_template

# parse_template(...)



# %% ------------ programme principal ------------------

import tools

print(f"Nom du module importé: {tools.__name__}")
print(f"Nom du module importé: {__name__}")
# le nom du module courant sera toujours __main__
# le nom d'un module importé sera toujouts le nom du fichier - l'extension

# 1. afficher le nom du programme principal: nom du module courant
# 2. afficher le nom d'un module importé
# 3. comment certifier qu'un code d'un module donné ne s'exécutera que si le module est principal
# cf => dans tools.py

# ici c'est une convention qui fait référence au int main(void){} en C
if __name__ == "__main__":
  tools.parse_template("blabla {{value}}", {"value": 50}, debug=True)
# %%
