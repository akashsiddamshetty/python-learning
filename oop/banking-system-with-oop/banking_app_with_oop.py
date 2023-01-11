# Parent Class

class User():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_details(self):
        print("Personal details")
        print(" ")
        print("Name -", self.name)
        print("Age -", self.age)
        print("Gender -", self.gender)

# Child Class


class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Account balance as been updated :", self.balance)

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance = self.balance-amount
            print("Account balance as been updaed :", self.balance)
        else:
            print("Insufficient balance")

    def view_balance(self):
        self.show_details()
        print("Account balance :", self.balance)


accountHolder = Bank('John', 24, 'male')
accountHolder.deposit(400)
accountHolder.withdraw(500)
accountHolder.withdraw(50)
accountHolder.view_balance()
