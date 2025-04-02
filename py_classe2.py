# person class
from datetime import date, datetime


class Person:
    def __init__(self, name, dob, gender, disabled):
        self.name = name
        self.dob = dob
        self.gender = gender
        self.disabled = disabled

    def print_details(self):
        print(f"Name:{self.name}")
        print(f"Dob:{self.dob}")
        print(f"Gender:{self.gender}")
        if self.disabled:
            print("disabled")
        else:
            print("Enabled")
        print("________________________")

    def get_age(self):
        current_date = datetime.today()
        date_birth = datetime.strptime(self.dob, "%d-%m-%Y")
        age = current_date - date_birth
        print("Age is ", age.days//365)


p1 = Person("Susan", "19-01-1967","Female", "False" )
p2 = Person("John", "12-12-1974", "Male", "True")

p1.print_details()
p2.print_details()

p1.get_age()
p2.get_age()
