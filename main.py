
#Requested user interface
    #Input:
    #Enter 1 to make a car, 2 to make a truck, or 3 to quit:

    #Please enter the car make:
    #Please enter the car model:
    #Please enter the number of doors:

    #Output:
    #The number of doors:
    #The make of is:
    #The model is:
    #Your car has been added to the garage

    #Loop/end
    #Enter 1 to make a car, 2 to make a truck or 3 to quit:

#Must include:
    #A Vehicle class that contains all the methods and attributes outlined in the class diagram below.
    #A Car class that is a child class of the Vehicle class with the methods and attributes detailed in the class diagram below. 
    #A Pickup class is a child class of the Vehicle class with the methods and attributes detailed in the class diagram below. 

import sys
class Vehicle:
    def __init__(self):
        self.VehicleMake = ""
        self.VehicleModel = ""
    
    def SetVehicleMake(self, make):
        self.VehicleMake = make

    def SetVehicleModel(self, model):
        self.VehicleModel = model
    
    def GetVehicleMake(self):
        return self.VehicleMake
    
    def GetVehicleModel(self):
        return self.VehicleModel
    
class Car(Vehicle):
    def __init__(self):
        super().__init__()
        self.CarDoor = ""

    def SetCarDoor(self, door):
        self.CarDoor = door

    def GetCarDoor(self):
        return self.CarDoor

class Truck(Vehicle):
    def __init__(self):
        super().__init__()
        self.BedLength = ""
    
    def SetBedLength(self, length):
        self.BedLength = length
    
    def GetBedLength(self):
        return self.BedLength
run = True
while run is True:
    print("Enter 1 to make a car, 2 to make a truck, or 3 to quit:")
    choice = input()

    if choice == "1":
        new_car = Car()
        new_car.SetVehicleMake(input("Please enter the car make:"))
        new_car.SetVehicleModel(input("Please enter the car model:"))
        new_car.SetCarDoor(input("Please enter the number of doors:"))
        
        print("The make of is:", new_car.GetVehicleMake())
        print("The model is:", new_car.GetVehicleModel())
        print("The number of doors:",new_car.GetCarDoor())
        print("Your car has been added to the garage")
    
    if choice == "2":
        new_truck = Truck()
        new_truck.SetVehicleMake(input("Please enter the car make:"))
        new_truck.SetVehicleModel(input("Please enter the car model:"))
        new_truck.SetBedLength(input("Please enter the bed length:"))
        
        print("The make of is:", new_truck.GetVehicleMake())
        print("The model is:", new_truck.GetVehicleModel())
        print("The number of doors:",new_truck.GetBedLength())
        print("Your car has been added to the garage")
    if choice =="3":
        sys.exit()
    else:
        print("Invalid input, please try again.")
        