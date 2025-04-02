# inheritance



class Person:
    def __init__(self, name:str, age:int):
        self.name = name.capitalize()
        if age > 100:
              raise Exception("You can't go over 100 years")
        self.age = age

    def print_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

class Student(Person): # inherit everything
    def __init__(self, name:str, age:int, courses:list, adm_number:str):
        super().__init__(name, age) # called from the parent class
        self.courses = courses
        self.adm_number = adm_number

    def print_details(self):
        super().print_details()
        print(f"Courses: {self.courses}")
        print(f"Adm number: {self.adm_number}")

s1 = Student("Malia", 22, ["Maths", "Geo"], "ADM24298")

s1.print_details()


# p1 = Person("KaMau", 94)

# p1.print_details()








