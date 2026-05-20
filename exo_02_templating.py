# %%
"""
exercice : remplacer les clés entourées par "((" et "))"
dans un texte par les valeurs correspondantes dans un dico

1. afficher le contenu entre la première occurence de (( et ))
2. remplacer ((pression)) par 500 dans _template
Hint: regarder la fonction str.replace
3. itérer sur _template pour remplacer toutes les slots (())
par la clé correspondante si celle ci existe ou par N/A
"""

_template = """
robinet.pression=((pression))
robinet.section=((section))
robinet.debit=((debit))
robinet.capacite=((capacite))
"""

injections = {
    "pression": "500",
    "section": "30",
    "debit": "2"
}

# %%
# avec while
# while _template.count("(("):
while "((" in _template:
  index_start = _template.index("((") + 2
  index_end = _template.index("))")
  key = _template[index_start:index_end]

  _template = _template.replace("((" + key + "))", injections.get(key, "N/A"))

print(_template)


# %%
# 1ère occurence
index_start = _template.index("((") + 2
index_end = _template.index("))")
key = _template[index_start:index_end]
print(key)

_template = _template.replace("((" + key + "))", injections[key])

# %%

# for sur le dico mais ne peux pas traiter les 
# valeurs qu'il ne connaît pas

for k, v in injections.items():
  _template = _template.replace("((" + k + "))", v)

print(_template)
# %%
# avec for qui détermine ex ante le nb de remplacement à faire
# "_" => je n'utilise pas la variable locale du bloc for
for _ in range(_template.count("((")):
  index_start = _template.index("((") + 2
  index_end = _template.index("))")
  key = _template[index_start:index_end]

  _template = _template.replace("((" + key + "))", injections.get(key, "N/A"))
print(_template)
# %%

## porter le code du while ou du for en fonction
## 0/ copier coller le code et l'entourer avec le bloc def ????():
## 1/ vous nommez la fonction de façon pertinente
## 2/ gérer la valeur de retour
## 3/ trouver les paramètres pertinents (positionnels/obligatoires), nommés avec defaut, *, **
## 4/ faire le refactoring: remplacer les variables globales de bout de code d'origine par les paramètres

def parse_template(
    tpl: str, 
    values: dict, 
    sep_in: str="{{", 
    sep_out: str="}}", 
    default: str="N/A",
    **opts
  ):
  for _ in range(tpl.count(sep_in)):
    index_start = tpl.index(sep_in) + len(sep_in)
    index_end = tpl.index(sep_out)
    key = tpl[index_start:index_end]
    if "debug" in opts and opts["debug"]:
      print(f"debug: key: {key}")

    tpl = tpl.replace(sep_in + key + sep_out, str(values.get(key, default)))
  return tpl

print(parse_template(_template, injections, sep_out="))", sep_in="(("))

print(parse_template("machin: {{clef}}", {"clef": 33}))
# %%
