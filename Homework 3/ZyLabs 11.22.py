#Ismael Diaz (PSID: 1846093)
#CIS 2348 Homework #3 Zylabs 11.22

rawinput = input()
splitlist = rawinput.split(" ")

for word in splitlist:
    print(word, splitlist.count(word))

