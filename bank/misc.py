from datetime import datetime

class Account:
  
  def __init__(self, balance: float, overdraft: float=200) -> None:
    self.balance = balance
    self.overdraft = overdraft
  
  ## comportement en affichage et en conversion en str
  def __str__(self):
    return f"account: {self.balance} with {self.overdraft}"

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

class Client:
  def __init__(self, firstname: str, lastname: str, date_str: str, date_format: str="%Y-%m-%d"):
    self.firstname = firstname
    self.lastname = lastname
    self.date_joint = datetime.strptime(date_str, date_format)
  
  def get_fullname(self) -> str:
    return f"{self.firstname.capitalize()} {self.lastname.upper()}"