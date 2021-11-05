#Ismael Diaz (PSID: 1846093)
#CIS 2348 Final Project Pt. 1
from datetime import date
from datetime import datetime
import csv
from fileinput import close

inventory = []
todaysdate = date.today()

#populating the master inventory
inputFile = open('ManufacturerList.csv')
reader = csv.reader(inputFile)

for items in reader:
    i = 0
    inventory.insert(i, [items[0], items[1], items[2]])
    i += 1

inputFile.close()

#importing prices and appending to inventory
inputFile = open('PriceList.csv')
reader = csv.reader(inputFile)

for prices in reader:
    for list in inventory:
        i = 0
        if prices[0] == list[0]:
            list.append(prices[1])
        i += 1

inputFile.close()

#importing service dates and appending to inventory
inputFile = open('ServiceDatesList.csv')
reader = csv.reader(inputFile)

for dates in reader:
    for list in inventory:
        i = 0
        if dates[0] == list[0]:
            list.append(dates[1])
        i += 1

inputFile.close()

#appending damaged attribute to the end of list for correct csv writing order
inputFile = open('ManufacturerList.csv')
reader = csv.reader(inputFile)

for damaged in reader:
    for list in inventory:
        i = 0
        if damaged[0] == list[0]:
            list.append(damaged[3])
        i += 1

inputFile.close()

#sorting and writing to fullinventory.csv
outputFile = open('FullInventory.csv', 'w', newline='')
writer = csv.writer(outputFile)

alphaInventory = sorted(inventory, key=lambda x: x[1])
writer.writerows(alphaInventory)

outputFile.close()

'''
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

'''