import FileHandle

"""
This module stores the retrieveVehicleInput method, which allows the user to see a car's make, availability and odometer rating. Includes error handling
Written by Eli James, 20177630
Last edited on July 20th, 2020
"""

#loads the list of list of cars into a list called carDatabse using the FileHandleModule
carDatabase = FileHandle.readFromDatabase()

#accepts a vehicle ID as a parameter and prompts the user for whether they want that car's make, availability or odometer rating, then prints it to console. Includes try except statements for error handling of the user input
def retrieveVehicleInfo(vehicleID):
    while True:
        try:
            choice = int(input("Press 1 to see the car's odometer rating, Press 2 to see the car's availability, Press 3 to see the car's make: "))
        except ValueError:
            print("Woops, type 1, 2 or 3: ")
            continue
        else:
            break
    #iterates through the list to find the car in question, then prints its odometer rating
    if choice == 1:
        for i in range(len(carDatabase)):
            currentCar = carDatabase[i]
            if vehicleID in currentCar:
                odometerRating = currentCar[3]
                print(f"The car's odometer rating is {odometerRating}")
    #iterates through the list to find the car in question, then prints its availability          
    if choice == 2:
        for i in range(len(carDatabase)):
            currentCar = carDatabase[i]
            if vehicleID in currentCar:
                availability = currentCar[6]
                print(f"The car is {availability}")
    #iterates through the list to find the car in question, then prints its make
    if choice == 3:
        for i in range(len(carDatabase)):
            currentCar = carDatabase[i]
            if vehicleID in currentCar:
                carMake = currentCar[1]
                print(f"The car is a {carMake}")
                
#for testing           
if __name__ == "__main__":
    #retrieveVehicleInfo("12345")
    print("")