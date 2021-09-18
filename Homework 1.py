#Ismael Diaz (PSID: 1846093)
#CIS 2348 Homework #1

i = 0

print("Welcome to your Birthday Calculator!")
cmonth = int(input("The current month is: "))
while i != 1:
    if 0 < cmonth <= 12:
        i += 1
    else:
        print("Please enter a valid month!")
        cmonth = int(input("The current month is: "))
cday = int(input("The current day is: "))
while i != 2:
    if 0 < cday <= 31:
        i += 1
    else:
        print("Please enter a valid day!")
        cday = int(input("The current day is: "))
cyear = int(input("The current year is: "))

print("Please enter your birthdate!")
bmonth = int(input("Birth month: "))
while i != 3:
    if 0 < bmonth <= 12:
        i += 1
    else:
        print("Please enter a valid month!")
        bmonth = int(input("Birth month: "))
bday = int(input("Birth day: "))
while i != 4:
    if 0 < bday <= 31:
        i += 1
    else:
        print("Please enter a valid day!")
        bday = int(input("Birth day: "))
byear = int(input("Birth year: "))


if cday == bday and cmonth == bmonth:
    print("Happy Birthday!!")
elif cmonth <= bmonth and cday < bday:
    print("You are ", cyear - byear - 1, " years old.")
else:
    print("You are ", cyear - byear, " years old.")

