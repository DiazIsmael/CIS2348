# Ismael Diaz (PSID: 1846093)
# CIS 2348 Final Project Pt. 2
from datetime import date, datetime
import csv

inventory = []
today = date.today()

# populating the master inventory
inputFile = open('ManufacturerList.csv')
reader = csv.reader(inputFile)

for line in reader:
    i = 0
    inventory.insert(i, [line[0], line[1], line[2]])
    i += 1

inputFile.close()

# importing prices and appending to inventory
inputFile = open('PriceList.csv')
reader = csv.reader(inputFile)

for prices in reader:
    for item in inventory:
        i = 0
        if prices[0] == item[0]:
            item.append(prices[1])
        i += 1

inputFile.close()

# importing service dates and appending to inventory
inputFile = open('ServiceDatesList.csv')
reader = csv.reader(inputFile)

for dates in reader:
    for item in inventory:
        i = 0
        if dates[0] == item[0]:
            item.append(dates[1])
        i += 1

inputFile.close()

# appending damaged attribute to the end of list for correct csv writing order
inputFile = open('ManufacturerList.csv')
reader = csv.reader(inputFile)

for damaged in reader:
    for item in inventory:
        if damaged[0] == item[0]:
            item.append(damaged[3])

inputFile.close()

# sorting inventory by price, creating manufacturer and item type sets & querying user for their chosen item
inventory = sorted(inventory, key=lambda x: x[3])
manufacturerSet = {}
typeSet = {}
manuList = []
typeList = []

for item in inventory:
    manuList.append(item[1])
    typeList.append(item[2])

manufacturerSet = set(manuList)
typeSet = set(typeList)

userInput = input("What is the Manufacturer and Item Type that you're looking for?:\n")
userItems = []

# Interactive Inventory Query loop
while userInput != "q":
    userInput = userInput.split()
    manufacturerCount = 0
    typeCount = 0
    userItems = []
    itemType = ""
    itemManufacturer = ""

    # used for later input validation
    for word in userInput:
        if word in manufacturerSet:
            manufacturerCount += 1
    for word in userInput:
        if word in typeSet:
            typeCount += 1

    # Validating user input and Gathering user desired item
    if manufacturerCount == 1 and typeCount == 1:
        for item in inventory:
            if item[1] in userInput and item[2] in userInput and item[5] != "damaged":
                serviceDate = datetime.strptime(item[4], "%m/%d/%Y").date()
                itemManufacturer = item[1]
                itemType = item[2]
                if serviceDate > today:
                    userItems.append(item)
    else:
        print("No such item in inventory.")
        userInput = input("What is the Manufacturer and Item Type that you're looking for?:\n")
        continue

    # Outputting user desired item(s)
    try:
        if manufacturerCount == 1 and typeCount == 1:
            print("Your item is: {}, {}, {}, ${}".format(userItems[0][0], userItems[0][1], userItems[0][2], userItems[0][3]))
    except:
        print("No such item in inventory.")
        userInput = input("What is the Manufacturer and Item Type that you're looking for?:\n")
        continue

    # Outputting & validating possible alternative item
    if manufacturerCount == 1 and typeCount == 1:
        for item in inventory:
            if item[1] != itemManufacturer and item[2] == itemType and item[5] != "damaged":
                serviceDate = datetime.strptime(item[4], "%m/%d/%Y").date()
                if serviceDate > today:
                    userItems.append(item)

                    print("You may, also, consider: {}, {}, {}, ${}".format(userItems[1][0], userItems[1][1], userItems[1][2], userItems[1][3]))
                    break

    userInput = input("What is the Manufacturer and Item Type that you're looking for?:\n")
