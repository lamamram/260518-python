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


# importer un module === exécuter la totalité du code importé => pas de print
# print("coucou")