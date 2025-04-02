# car [make, model, date_of_make, drive_side]
# get_age
# allowed_in_kenya
# print.details
from datetime import datetime

class Car:
    def __init__(self, make, model, date_of_man, drive_side):
        self.make = make
        self.model = model
        self.date_of_man = date_of_man
        self.drive_side = drive_side

    def date_of_make(self):
        current_date = datetime.today()
        date_of_make = datetime.strptime(self.date_of_man, "%d-%m-%Y")
        age = (current_date - date_of_make).days // 365
        if self.age > 7
            print()
        print("Car age is", age, "years")


    def check_drive_side(self):
        if self.drive_side == "left":
            print("The car is left-hand drive.")
        elif self.drive_side == "right":
            print("The car is right-hand drive.")
        else:
            print("Invalid drive side information.")

# Example Usage
my_car = Car("Toyota", "Corolla", "15-08-2015", "left")
my_car.date_of_make()
my_car.check_drive_side()
