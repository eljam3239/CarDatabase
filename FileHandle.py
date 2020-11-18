from csv import reader
#I tried a painful amount of ways of working with csv file without the csv library, but I ultimately stopped being stubborn and read the links commented in this program to learn how to use the csv module so I could work with reading and writing the csv file easier

"""
This module contains the method that stores the csv file into a list of lists that is easier to work with and the module which writes output to the text file if the user chooses to view it that way
Written by Eli James, 20177630
Last Edited on July 20th, 2020
"""

#learned how to make list of lists from a csv file from: https://thispointer.com/python-read-csv-into-a-list-of-lists-or-tuples-or-dictionaries-import-csv-to-list/
#turns the csv file from onq into a list of lists
def readFromDatabase(): 
    with open('C:\\Users\\Eli\\Desktop\\python\\assignment2elijames\\database1.csv', 'r') as read_obj:
    #makes a reader object
        csv_reader = reader(read_obj)
    #get a list of lists
        carDatabase = list(csv_reader)
        
    return carDatabase



#tried to implement the text writing file from assignment 1, had some troubles
#instead I am using inspiration from a user on stackoverflow: https://stackoverflow.com/questions/899103/writing-a-list-to-a-file-with-python
#writes a list to a text file that the user can use as an alternative to the console to view the car information
def writeToOuputFile(alist):
    outputFile = open("C:\\Users\\Eli\\Desktop\\python\\assignment2elijames\\outputFile.txt", "w")

    for item in alist:

        outputFile.write('%s' % item + " ")

    outputFile.close
#used this for testing like once
def displayInventory(inventory):
    for i in range(len(inventory)):
        print(inventory[i])

#for testing
if __name__ == "__main__":
    inventory = readFromDatabase()
    displayInventory(inventory)
    
    writeToOuputFile('C:\\Users\\Eli\\Desktop\\python\\assignment2elijames\\outputFile.txt', [1, 2, 3, 4])

