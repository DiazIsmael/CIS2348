#Ismael Diaz (PSID: 1846093)
#CIS 2348 Homework #2
from datetime import date

months_dict = {"January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6, "July": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December": 12}
todaysdate = date.today()
userdate = date(1111, 11, 1)
rawdate = ""
inputFile = open("inputDates.txt", "r")

while rawdate != "-1":
    rawdate = inputFile.readline()

    x = rawdate.replace("\n", "")
    x = x.replace(",", "")
    x = x.split(" ")

    if x[0] in months_dict.keys() and 0 < int(x[1]) < 32 and len(x[2]) == 4:
        userdate = date(int(x[2]), int(months_dict[x[0]]), int(x[1]))
        if userdate < todaysdate:
            print("{}/{}/{}".format(months_dict[x[0]], x[1], x[2]))
        else:
            pass

inputFile.close()