#1) Создайте класс для банковского счета с методами пополнения, снятия и проверки баланса.
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} has been deposited to {self.name}'s account")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Insufficient balance in {self.name}'s account")
        else:
            self.balance -= amount
            print(f"{amount} has been withdrawn from {self.name}'s account")

    def check_balance(self):
        print(f"{self.name}'s current balance is {self.balance}")

account1 = BankAccount("Jane Doe", 5000)
account1.check_balance() 