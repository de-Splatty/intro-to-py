from datetime import datetime, date


class Car:
    def __init__(self, make, model, year_of_make, drive_side):
        self.make = make
        self.model = model
        self.year_of_make = year_of_make
        self.drive_side = drive_side

    def print_car_details(self):
        print(f"make:", self.make)
        print(f"model:", self.model)
        print(f"year of make:", self.year_of_make)
        print(f"drive side:", self.drive_side)

        if self.drive_side_right:
            print("Allowed in kenya")
        else:
            print("Not allowed in kenya")

    def get_age(self):
        current_date = date.today().date
        date_making = date.time(str(date.today()))
        
