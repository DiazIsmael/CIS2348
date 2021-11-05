#Ismael Diaz (PSID: 1846093)
#CIS 2348 Final Project Pt. 1
from datetime import date
from datetime import datetime
import csv
from fileinput import close

inventory = []
today = date.today()

# populating the master inventory
inputFile = open('ManufacturerList.csv')
reader = csv.reader(inputFile)

for items in reader:
    i = 0
    inventory.insert(i, [items[0], items[1], items[2]])
    i += 1

inputFile.close()

# importing prices and appending to inventory
inputFile = open('PriceList.csv')
reader = csv.reader(inputFile)

for prices in reader:
    for list in inventory:
        i = 0
        if prices[0] == list[0]:
            list.append(prices[1])
        i += 1

inputFile.close()

# importing service dates and appending to inventory
inputFile = open('ServiceDatesList.csv')
reader = csv.reader(inputFile)

for dates in reader:
    for list in inventory:
        i = 0
        if dates[0] == list[0]:
            list.append(dates[1])
        i += 1

inputFile.close()

# appending damaged attribute to the end of list for correct csv writing order
inputFile = open('ManufacturerList.csv')
reader = csv.reader(inputFile)

for damaged in reader:
    for list in inventory:
        if damaged[0] == list[0]:
            list.append(damaged[3])

inputFile.close()

# sorting and writing to fullInventory.csv
outputFile = open('FullInventory.csv', 'w', newline='')
writer = csv.writer(outputFile)

alphaInventory = sorted(inventory, key=lambda x: x[1])
writer.writerows(alphaInventory)

outputFile.close()

# sorting and writing item type inventory list to [itemtype]Inventory.csv
itemTypes = []
alphaInventory = sorted(inventory, key=lambda x: x[0])
itemInventory = []

for index in range(len(alphaInventory)):
    itemInventory.append([alphaInventory[index][0], alphaInventory[index][1], alphaInventory[index][3], alphaInventory[index][4], alphaInventory[index][5]])

i = 0
for list in alphaInventory:
    itemTypes.append(list[2])
    filename = itemTypes[i] + 'Inventory.csv'
    outputFile = open(filename, 'w', newline='')
    writer = csv.writer(outputFile)

    for item in alphaInventory:
        if list[2] == item[2]:
            for a in range(len(alphaInventory)):
                if item[0] == itemInventory[a][0]:
                    writer.writerow(itemInventory[a])

    i += 1

# PART C