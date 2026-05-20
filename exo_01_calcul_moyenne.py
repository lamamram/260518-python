# %%
"""
1/ saisir n valeurs entiers relatifs dans le clavier séparés par ","
2/ on veut itérer sur les valeurs saisies pour vérifier
que ces valeurs sont des entiers relatifs (1er cas entier naturel ensuite 2ème cas négatif)
3/ si c'est convertible on ajoute la valeur convertie dans une liste
3b/ si ce n'est pas convertible => "casser la boucle"
4/ calculer la moyenne depuis la liste
5/ présenter le résultat avec 2 chiffres sign.  
"""

# %%
# donées d'entrées
valeurs = input("saisir des entiers relatifs séparés par ,:")
# écrire une variable en dernière ligne d'une cellule et au niveau d'indentation 0 la rend affichable dans la console jupyter 
valeurs

# %%
candidates = valeurs.split(",")
candidates

# %%
# initialiser les listes pour traiter les saisies
integers, errors = [], []
for candidat in candidates:
  # nettoyer les espaces à gauche et à droite
  candidat = candidat.strip()
  # la chaine de caractère représente des chiffres OU (une chaine qui commence avec "-" ET le reste est fait de chiffres)
  # ==> représente un entier relatif DONC convertible
  if candidat.isnumeric() or (candidat.startswith("-") and candidat[1:].isnumeric()):
    integers.append(int(candidat))
  else:
    if candidat:
      errors.append(candidat)
  
integers

# %%
# s'il n'y a pas d'erreurs ==> si errors est la liste vide []
if not errors:
  # s'il ya des integers ==> si intergers contient des nombres ==> n'est PAS []
  if integers:
    avg = round(sum(integers) / len(integers), 2)
    print(f"moyenne à 2 décimales sign. de { integers }: {avg}")
  else:
    print("liste vide !!!!")
else:
  print(f"valeurs défectueuses: {errors}")