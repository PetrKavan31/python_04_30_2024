import pickle
import json

# Supplement the Car class with the ability to pack and unpack data using json and pickle.

# Implement a class Car. Class fields should store the following:
# model, year of release, manufacturer, engine capacity,
# color, price. Implement class methods for data input and output,
# provide access to individual fields through class methods.


class Car:
    type = "Passenger car"

    def __init__(self, model, year_of_release, manufacturer, engine_capacity, color, price):
        self.model = model
        self.year = year_of_release
        self.manufacturer = manufacturer
        self.engine = engine_capacity
        self.color = color
        self.price = price

    def show_car(self):
        print("My car:\n", self.model, self.year, self.manufacturer, self.engine, self.color, self.price)

    def show_owner(self, text_msg):
        return f"Owner car {self.manufacturer} {self.model} is {text_msg}"


car1 = Car("Civic", 2004, "Honda", 1.6, "grey", 1500)
car2 = Car("Fusion", 2010, "Ford", 1.4, "red", 5000)

car1.show_car()
car2.show_car()

print(car1.model)
print(car2.color)

print(car1.show_owner("Petr"))
print(car2.show_owner("Marketa"))

car2.model = "Fiesta"
print(car2.model)
car2.show_car()

print(car1.type)
print(car2.type)