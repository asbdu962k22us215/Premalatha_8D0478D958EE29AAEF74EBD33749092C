#Implement a class called BankAccount that represents a bank account. The class should have private attributes for account number, account holder name, and account balance. Include methods to deposit money, withdraw money, and display the account balance. Ensure that the account balance cannot be accessed directly from outside the class. Write a program to create an instance of the BankAccount class and test the deposit and withdrawal functionality. 



class Bank_Account:
  def __init__(self):
    self.__name=str(input("Enter the name of account holder:"))
    self.__ano=int(input("Enter the type of account number:"))
    self.__balance=0
    print("Hello!!! Welcome to the Deposit and Withdrawal machine")
  def deposit(self):
    self.__amount=float(input("Enter amount to be deposited:"))
    if self.__amount>0:
      self.__balance += self.__amount
      print("\n Amount deposited:",self.__amount)
  def withdraw(self):
    __amount=float(input("Enter amount to be withdrawn:"))
    if self.__balance>=__amount:
      self.__balance-=__amount
      print("\n You withdraw:",__amount)
      print("\n Balance:",self.__balance)
    else:
      print("\n Insufficient balance")
  def display(self):
    print("\n Account holder name:",self.__name)
    print("\n Account number:",self.__ano)
    print("\n Net available balance:",self.__balance)
s= Bank_Account()
s.deposit()
s.withdraw()
s.display()
      