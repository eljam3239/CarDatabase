import FileHandle
import csv 
#explain csv library in FileHandle.py

"""
Contains the majority of the functions in the program, which add cars, update their info, view their info and perform keyword searches of the database
Written by Elijah James, 20177630
Last edited on July 20th, 2020
"""

#creates the list of lists that temporarily stores the car database (easier to work with than the CSV file itself). Gets written to the database later on.
carDatabase = []
carDatabase = FileHandle.readFromDatabase()

#This function allows users to add a car to the database. Includes error handling for if the user tries to enter something that doesn't make sense, such as its make being Fo23rd, for example. 
#got stuck on error handling, learned try/except/else from 101computing.net
#saves the new car to the csv file
def addNewVehicle():
    newCar = []
    #asks for the vehicle ID
    while True:
        try:
            vehicleID = int(input("Please input the vehicle's ID, composed of 5 integers: "))
                 
        except ValueError:
            print("Not an integer, try again!")
            continue
        else:
            newCar.append(vehicleID)
            break
    #asks for the car make
    while True:
        try:
            carMake = str(input("Please input the vehicle's car make (ex: Ford): "))
                
        except ValueError:
            print("Not an valid string, try again!")
            continue
        else:
            newCar.append(carMake)
            break
    
    while True:
        try:
            carType = str(input("Please input the vehicle's car type (ex: Escape): "))
                
        except ValueError:
            print("Not an valid string, try again!")
            continue
        else:
            newCar.append(carType)
            break
    while True:
        try:
            carOdometer = int(input("Please input the vehicle's odometer rating to the nearest integer number: "))
                
        except ValueError:
            print("Not an valid integer, try again! (ex: 14500): ")
            continue
        else:
            newCar.append(carOdometer)
            break
    while True:
        try:
            carCost = float(input("Please input the vehicle's cost to rent per day, to the nearest cent (ex: 54.50): "))
                
        except ValueError:
            print("Not an valid cost, try again!")
            continue
        else:
            newCar.append(carCost)
            break
    while True:
        try:
            timesRented = int(input("Please input the number of times the vehicle has been rented: "))
                
        except ValueError:
            print("Not an valid number, try again!")
            continue
        else:
            newCar.append(timesRented)
            break
    while True:
        try:
            carAvailability = str(input("Please input the vehicle's availability ('Available' or 'Unavailable') "))
                
        except ValueError:
            print("You didn't type 'Available' or 'Unavailable', try again: ")
            continue
        else:
            newCar.append(carAvailability)
            break
    #adds the list that contains the new car info to the list of lists, which is the database. 
    carDatabase.append(newCar)
    #saves the new database to a csv file, from which it can be read later on if needed
    with open('C:\\Users\\Eli\\Desktop\\python\\assignment2elijames\\database1.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(carDatabase)

#this function takes a car's vehicle Id, then allows the user to update its odometer rating(which is illegal I think lol), its cost to rent per day, and its availability
# saves the update to the csv file
# includes error handling for ValueErrors when inputting the options to make sure the method runs smoothly    
def updateVehicleInfo(vehicleID):
    
    while True:
        try:
            choice = int(input("Press 1 to update this car's odometer rating, 2 to update it's cost to rent per day or 3 to update the rental status of the vehicle: "))
        except ValueError:
            print("Not an valid number, try again!")
            continue
        if choice not in range(1, 4):
            print("Not a valid number, try again!")
            continue
        else:
            break
    
    if choice == 1: #updates the odometer rating
        while True:
            try:
                odomUpdate = int(input("Please input a new odometer rating: "))
            except ValueError:
                print("Not an valid number, try again!")
                continue
            
            else:
                break
        for i in range(len(carDatabase)):
            
            if vehicleID == carDatabase[i][0]:
                carDatabase[i][3] = odomUpdate
                        
    if choice == 2: #updates the cost to rent per day
        while True:
            try:
                costUpdate = float(input("Please input a new cost to rent per day for this car: "))
            except ValueError:
                print("Not an valid number, try again!")
                continue
            
            else:
                
                for i in range(len(carDatabase)):
                    currentCar = carDatabase[i]
                    if vehicleID == currentCar[0]:
                        currentCar[4] = costUpdate
                        i+=1
                    else:
                        i+=1
                
                #print(carDatabase)
                
                break

    if choice == 3: #updates the availability of the vehicle
        while True:
            try:
                availabilityUpdate = str(input("Please input 'Available' or 'Unavailable': "))
            except ValueError:
                print("Type 'Available' or 'Unavailable': ")
                continue
           
            
            else:
                
                for i in range(len(carDatabase)):
                    currentCar = carDatabase[i]
                    if vehicleID == currentCar[0]:
                        currentCar[6] = availabilityUpdate
                        i+=1
                    else:
                        i+=1
                
                
                break
    #saves the new car info to the csv file
    #tried a painful amount of ways to write to csv file, ultimately used this tutorial: https://docs.python.org/3/library/csv.html
    with open('C:\\Users\\Eli\\Desktop\\python\\assignment2elijames\\database1.csv', 'w', newline='') as g:
        writer = csv.writer(g)
        writer.writerows(carDatabase)
    
#allows the user to pritn all the vehicles by type, make or availability either to the console or to the outFile.txt file. Includes error handling for if the user enters a valueError while choosing what they wanna do
def displayVehicleInformation():
    #stores what thing they wanna display
    while True:
            try:
                choice= int(input("Press 1 to see all the info for all the vehicles, press 2 to  list all vehicles by make, type or availability, or press 3 to retrieve a list of the vehicle IDs corresponding to a make: "))
            except ValueError:
                print("Woops, you have to input 1, 2 or 3 for the options above: ")
                continue
            if choice not in range(1, 4):
                print("Woops, only 1, 2 and 3 are valid entries, try again: ")
                continue
            
            else:
                break
    #stores the option for how they want to display it(console or text file)
    while True:
            try:
                outputOption= int(input("Press 1 to output to console, or press 2 to output to outputFile.txt: "))
            except ValueError:
                print("Woops, you have to input 1 or 2 for the options above: ")
                continue
            if outputOption not in range(1, 3):
                print("Woops, only 1 and 2 are valid entries, try again: ")
                continue
            
            else:
                break
    #if they wanna see the whole database in console
    if choice == 1 and outputOption == 1: 
        print(carDatabase)
    #if they wanna see the whole database in the output text file
    elif choice == 1 and outputOption == 2:
        FileHandle.writeToOuputFile(carDatabase)
    
    #if they wanna see all vehicles by type/make/avaialbility in console
    if choice == 2 and outputOption == 1:
        #figures out if they wanna see make, type or availability of all vehicles
        while True:
            try:
                subChoice2 = int(input("Press 1 to view all vehicles by make, 2 to list them all by type or 3 to list them all by availability: "))
            except ValueError:
                print("Woops, type 1, 2 or 3 for the options above: ")
                continue
            if subChoice2 not in range(1, 4):
                print("Woops! Type a number between 1 and 3 for the options above: ")
            else:
                break
        #shows all vehicles by make in console       
        if subChoice2 == 1:
            for i in range(len(carDatabase)):
                try:
                    print(f"Car {carDatabase[i][0]}: {carDatabase[i][1]}")
                except IndexError:
                    continue
        #shows all vehicles by type in console
        if subChoice2 ==2:
            for i in range(len(carDatabase)):
                try:
                    print(f"Car {carDatabase[i][0]}: {carDatabase[i][2]}")
                except IndexError:
                    continue
        #shows all vehicles by availability in console
        if subChoice2 == 3:
            for i in range(len(carDatabase)):
                try:
                    print(f"Car {carDatabase[i][0]}: {carDatabase[i][6]}")
                except IndexError:
                    continue
    #if they wanna see all vehicles by type/make/avaialbility in the output text file
    if choice == 2 and outputOption == 2:
        #figures out if they wanna see make, type or availability of all vehicles
        while True:
            try:
                subChoice2 = int(input("Press 1 to view all vehicles by make, 2 to list them all by type or 3 to list them all by availability: "))
            except ValueError:
                print("Woops, type 1, 2 or 3 for the options above: ")
                continue
            if subChoice2 not in range(1, 4):
                print("Woops! Type a number between 1 and 3 for the options above: ")
            else:
                break
        
        #shows all vehicles by make in text file       
        if subChoice2 == 1:
            returnList = []
            for i in range(len(carDatabase)):
                try:
                    returnList.append(carDatabase[i][1])
                    FileHandle.writeToOuputFile(returnList)
                except IndexError:
                    continue
        #shows all vehicles by type in text file
        if subChoice2 ==2:
            returnList = []
            for i in range(len(carDatabase)):
                try:
                    returnList.append(carDatabase[i][2])
                    FileHandle.writeToOuputFile(returnList)
                except IndexError:
                    continue
        #shows all vehicles by availability in text file
        if subChoice2 == 3:
            returnList = []
            for i in range(len(carDatabase)):
                try:
                    returnList.append(carDatabase[i][6])
                    FileHandle.writeToOuputFile(returnList)
                except IndexError:
                    continue
    #shows IDs associated with a make to console, has error handling for same reason as above
    if choice == 3 and outputOption == 1:
        
        correspondingIDs = []
       
        while True:
            try:
                make = (input("Please enter a valid vehicle make (ex Ford): "))
            except ValueError:
                print("Woops: Enter a valid string: ")
                continue
            else:
                break
        for j in range(len(carDatabase)):
                    if make == carDatabase[j][1]:
                        correspondingIDs.append(carDatabase[j][0]) 
        
        print(f"The following vehicle ID's correspond to the car make you entered: {correspondingIDs}")
    #shows Ids associated with a make to text file, has error handling for same reason as above
    if choice == 3 and outputOption == 2:
        
        correspondingIDs = []

        while True:
            try:
                make = (input("Please enter a valid vehicle make (ex Ford): "))
            except ValueError:
                print("Woops: Enter a valid string: ")
                continue
            else:
                break
        for j in range(len(carDatabase)):
                    if make == carDatabase[j][1]:
                        correspondingIDs.append(carDatabase[j][0]) 
        FileHandle.writeToOuputFile(correspondingIDs)
#will print all info for a vehicle containing a keyword inputed by the user to console or to a text file          
def keyWordSearch():
    #asks the user if they wanna see the results of the keyword search to console or to the text file
    while True:
        try:
            outputOption = int(input("Press 1 to have the results of your keyword search printed to console or 2 to have it put into the outputFile.txt file: "))
        except ValueError:
            print("Not an valid number, try again!")
            continue
        if outputOption not in range(1, 3):
            print("Not a valid number, try again!")
            continue
        else:
            break
    #stores the keyword to search for in the database
    while True:
        try:
            keyWord = (input("Please enter a keyword to search for in the database: "))
        except ValueError:
            print("Please try again; input a string: ")
            continue
        else:
            break
    #case sensitive, prints the list that the keyword is in to console    
    if outputOption == 1:
        for i in range(len(carDatabase)):
            
            if keyWord in carDatabase[i]:
                print(carDatabase[i])
    #case sensitive, prints the list that the keyword is in to the text file
    elif outputOption == 2:
        outputList = []
        for j in range(len(carDatabase)):
            
            if keyWord in carDatabase[j]:
                outputList.append(carDatabase[j])
        FileHandle.writeToOuputFile(outputList)
#i used this for testing
if __name__ == "__main__":
    #addNewVehicle()
    #updateVehicleInfo('44444')
    #displayVehicleInformation()
    #keyWordSearch()
    print("")
