# classes are written with first letter in uppercase
class Account:
    def __init__(self, acc__number, name, balance):
        self.acc__number = acc__number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit was successful. Balance is {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Balance")
        else:
            self.balance -= amount

    def details(self):
        print(f"Account number : {self.acc__number}")
        print(f"Name: {self.name}")
        print(f"Balance: {self.balance}")
        print("_____________________")

acc1 = Account("001", "Justin Muturi", 30000000)
acc2 = Account("002", "Millie Odhiambo", 200000000)

acc1.deposit(1000000)
acc1.withdraw(200000)
acc1.details()