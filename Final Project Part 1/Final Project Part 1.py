#Ismael Diaz (PSID: 1846093)
#CIS 2348 Final Project Pt. 1
from datetime import date, datetime
import csv

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
sortedInventory = sorted(inventory, key=lambda x: x[0])
itemInventory = []
itemTypes = []

for index in range(len(sortedInventory)):
    itemInventory.append([sortedInventory[index][0], sortedInventory[index][1], sortedInventory[index][3], sortedInventory[index][4], sortedInventory[index][5]])

i = 0
for list in sortedInventory:
    itemTypes.append(list[2])
    filename = itemTypes[i] + 'Inventory.csv'
    outputFile = open(filename, 'w', newline='')
    writer = csv.writer(outputFile)

    for item in sortedInventory:
        if list[2] == item[2]:
            for a in range(len(sortedInventory)):
                if item[0] == itemInventory[a][0]:
                    writer.writerow(itemInventory[a])

    outputFile.close()
    i += 1

# sorting dates and writing to PastServiceDateInventory.csv
outputFile = open("PastServiceDateInventory.csv", 'w', newline='')
writer = csv.writer(outputFile)
sortedInventory = []

i = 0
for list in inventory:
    dateobject = datetime.strptime(inventory[i][4], "%m/%d/%Y").date()
    sortedInventory.append([inventory[i][0], inventory[i][1], inventory[i][2], inventory[i][3], dateobject, inventory[i][5]])
    i += 1

sortedInventory = sorted(sortedInventory, key=lambda x: x[4])

i = 0
for list in sortedInventory:
    if list[4] < today:
        date = list[4]
        writer.writerow([inventory[i][0], inventory[i][1], inventory[i][2], inventory[i][3], date.strftime("%m/%d/%Y"), inventory[i][5]])

    i += 1

# sorting prices and writing to DamagedInventory.csv
