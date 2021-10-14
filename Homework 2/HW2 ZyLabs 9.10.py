#Ismael Diaz (PSID: 1846093)
#CIS 2348 Homework #2 Zylabs 9.10

from csv import reader

tally = {}
fileName = input()

inputFile = open(fileName)
csvreader = reader(inputFile, delimiter=",")
lines = []

for lines in csvreader:
    for i in lines:
        if i in tally.keys():
            tally[i] = tally[i] + 1
        else:
            tally[i] = 1

for word in list(tally.keys()):
    print(word, tally[word])

inputFile.close()
