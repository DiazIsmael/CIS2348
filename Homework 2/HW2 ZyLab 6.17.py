#Ismael Diaz (PSID: 1846093)
#CIS 2348 Homework #2 Zylabs 6.17

rawpassword = input()
newpassword = ""

for char in rawpassword:
    if char == "i":
        newpassword = newpassword + "!"
    elif char == "a":
        newpassword = newpassword + "@"
    elif char == "m":
        newpassword = newpassword + "M"
    elif char == "B":
        newpassword = newpassword + "8"
    elif char == "o":
        newpassword = newpassword + "."
    else:
        newpassword = newpassword + char
newpassword = newpassword + "q*s"

print(newpassword)