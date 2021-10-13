#Ismael Diaz (PSID: 1846093)
#CIS 2348 Homework #1 Zylabs 2.19

ljuice = float(input("Enter amount of lemon juice (in cups):\n"))
water = float(input("Enter amount of water (in cups):\n"))
anectar = float(input("Enter amount of agave nectar (in cups):\n"))
servings = float(input("How many servings does this make?\n"))
print()

print("Lemonade ingredients - yields", "{:.2f}".format(servings), "servings")
print("{:.2f}".format(ljuice), "cup(s) lemon juice")
print("{:.2f}".format(water), "cup(s) water")
print("{:.2f}".format(anectar), "cup(s) agave nectar")
print()

newservings = float(input("How many servings would you like to make?\n"))
ratio = newservings/servings
print()
print("Lemonade ingredients - yields", "{:.2f}".format(newservings), "servings")
print("{:.2f}".format(ljuice*ratio), "cup(s) lemon juice")
print("{:.2f}".format(water*ratio), "cup(s) water")
print("{:.2f}".format(anectar*ratio), "cup(s) agave nectar")
print()
print("Lemonade ingredients - yields", "{:.2f}".format(newservings), "servings")
print("{:.2f}".format((ljuice*ratio)/16), "gallon(s) lemon juice")
print("{:.2f}".format((water*ratio)/16), "gallon(s) water")
print("{:.2f}".format((anectar*ratio)/16), "gallon(s) agave nectar")