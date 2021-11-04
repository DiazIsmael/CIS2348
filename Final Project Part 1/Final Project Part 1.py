#Ismael Diaz (PSID: 1846093)
#CIS 2348 Final Project Pt. 1
from datetime import date
from datetime import datetime
import csv
from fileinput import close

inventory = {}
todaysdate = date.today()

#populating the master inventory dictionary
inputFile = open('ManufacturerList.csv')
reader = csv.reader(inputFile)

for item in reader:
    inventory[item[0]] = [item[1], item[2]]

inputFile.close()

#importing prices and appending to inventory dictionary
inputFile = open('PriceList.csv')
reader = csv.reader(inputFile)

for item in reader:
    inventory[item[0]].append(item[1])

inputFile.close()

#importing service dates and appending to inventory dict
inputFile = open('ServiceDatesList.csv')
reader = csv.reader(inputFile)

for item in reader:
    inventory[item[0]].append(item[1])

inputFile.close()

#appending damaged attribute to the end of list
inputFile = open('ManufacturerList.csv')
reader = csv.reader(inputFile)

for item in reader:
    inventory[item[0]].append(item[3])

inputFile.close()

#sorting and writing to fullinventory.csv
outputFile = open('FullInventory.csv', 'w')
writer = csv.writer(outputFile)

sortedInventory = {}
sortedList = sorted(inventory.values())

for list in sortedList:
    for key in inventory.keys():
        if inventory[key] == list:
            sortedInventory[key] = inventory[key]

writer.writerow(sortedInventory.items())
print(sortedInventory)

"""outputList = []

for keys in sortedInventory.keys():
    outputList.append(keys)
    for values in sortedInventory.values():
        outputList.append(sortedInventory[keys])

print(outputList)"""