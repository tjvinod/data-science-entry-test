class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def describe_car(self):
        print(f"{self.year} {self.make} {self.model}")

# Task 2
my_car = Car("Toyota", "Corolla", 2020)
my_car.describe_car()