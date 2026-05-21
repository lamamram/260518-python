from datetime import datetime

class Client:
  def __init__(self, firstname: str, lastname: str, date_str: str, date_format: str="%Y-%m-%d"):
    self.firstname = firstname
    self.lastname = lastname
    self.date_joint = datetime.strptime(date_str, date_format)
  
  def get_fullname(self) -> str:
    return f"{self.firstname.capitalize()} {self.lastname.upper()}"

class Account:
  
  def __init__(self, client: Client, balance: float, overdraft: float=200) -> None:
    self.balance = balance
    self.overdraft = overdraft
    self.client = client
  
  ## comportement en affichage et en conversion en str
  def __str__(self):
    return f"account: {self.balance} with {self.overdraft}"

  ## comportement en ajout (+)
  ## les méthodes permettent d'ajouter des comportement aux objets custom
  def __add__(self, acc):
    return self.balance + acc.balance

  def withdraw(self, amount: float):
    if amount < 0:
      print(f"Transaction refusée: {amount} négatif")
    elif amount > self.balance + self.overdraft:
      print(f"Transaction refusée: {amount} fonds insuffisants")
    else:
      self.balance -= amount
      print(f"Transaction acceptée")
  
  def set_10birthday_bonus(self):
    now = datetime.now()
    now_year, now_month, now_day = now.year, now.month, now.day
    cl_year, cl_month, cl_day = self.client.date_joint.year, self.client.date_joint.month, self.client.date_joint.day
    if now_year - cl_year == 10 and now_month == cl_month and now_day == cl_day:
      self.balance += 100
