import FileHandle
import Commands
import Database

"""
This is the driver module, created by Elijah James, 20177630
Last modified on July 20th, 2020
This program adds vehicles to a database, allows users to edit info about these vehicles, allows the user to view the information for the vehicles, and allows the user to perform keyword searches throughtought the databse to see what vehicles are relavent to their search
"""

#main function, which acts as the interface with which users call the functions
def main():
    #this loop promts the user for an input corrsponding to one of the functions and catches user input errors, allowing the program to run seamlessly
    while True:
        
        try:
            command = int(input("welcome to the car inventory program!\nEnter 1 to add a vehicle to inventory, 2 to update a vehicle's information, 3 to display a vehicle's information, 4 to perform a keyoword search in the database or 5 to see the odometer rating, availability or make of a specific car: "))
        except ValueError:
            print("Woops, you didn't enter 1, 2, 3, 4 or 5, try again: ")
        if command not in range(1, 6):
            print("Woops, you didn't enter 1, 2, 3, 4 or 5, try again: ")
        else:
            break
    #calls the funciton which allows users to add vehicles to the system
    if command == 1:
        Commands.addNewVehicle()
    #asks the user for a vehicle ID, and calls the funciton allowing them to update that vehicle's information, if it doesn;t have an error input, which it will catch
    elif command == 2:
        while True:
        
            try:
                car = (input("Please enter the vehicle ID of the car that you want to update (ex: 12345): "))
            except ValueError:
                print("Woops, you didn't enter a valid integer vehicle ID, try again: ")
            else:
                break
        Commands.updateVehicleInfo(car)
    #calls the function which allows users to display information for cars
    elif command == 3:
        Commands.displayVehicleInformation()
    #allows the user to perform a keyword search of the database 
    elif command == 4:
        Commands.keyWordSearch()
    #alllows the user to output the rating, availability or make of a vehicle, and catches user input error
    elif command == 5:
        while True:
        
            try:
                car = (input("Please enter the vehicle ID of the car that you want to see the rating, availability or make for (ex: 12345): "))
            except ValueError:
                print("Woops, you didn't enter a valid integer vehicle ID, try again: ")
            else:
                break
        Database.retrieveVehicleInfo(car)

main()