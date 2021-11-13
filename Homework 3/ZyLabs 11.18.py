#Ismael Diaz (PSID: 1846093)
#CIS 2348 Homework #3 Zylabs 11.18

rawinput = input()
rawlist = rawinput.split(" ")
sortedlist = []

for num in rawlist:
    if "-" in num:
        pass
    else:
        sortedlist.append(int(num))

for num in sortedlist:
    if num < 0:
        sortedlist.remove(num)

sortedlist.sort()
for num in sortedlist:
    print(num, end=" ")