# Name: Julian Paiz
# File Name: vehicle.py
# Description: This program collects information about a car
# and displays the vehicle information.

class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type


class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof


vehicle_type = "car"

year = input("Enter the year of the car: ")
make = input("Enter the make of the car: ")
model = input("Enter the model of the car: ")
doors = input("Enter the number of doors (2 or 4): ")
roof = input("Enter the type of roof (solid or sun roof): ")

car = Automobile(vehicle_type, year, make, model, doors, roof)

print()
print("Vehicle Information")
print("-------------------")
print("Vehicle type:", car.vehicle_type)
print("Year:", car.year)
print("Make:", car.make)
print("Model:", car.model)
print("Number of doors:", car.doors)
print("Type of roof:", car.roof)
