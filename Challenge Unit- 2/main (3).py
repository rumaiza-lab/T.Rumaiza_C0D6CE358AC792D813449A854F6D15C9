class BankAccount:
  def __init__(self, account_number, account_holder_name, account_balance=0):
      self.__account_number = account_number
      self.__account_holder_name = account_holder_name
      self.__account_balance = account_balance

  def deposit(self, amount):
      self.__account_balance += amount
      return self.__account_balance

  def withdraw(self, amount):
      if amount > self.__account_balance:
          print("Insufficient balance. Cannot withdraw.")
          return self.__account_balance
      self.__account_balance -= amount
      return self.__account_balance

  def display_balance(self):
      return self.__account_balance


account1 = BankAccount(12345, "Joe")

account1.deposit(1000)
print("Account balance after deposit: ", account1.display_balance())

account1.withdraw(500)
print("Account balance after withdrawal: ", account1.display_balance())
