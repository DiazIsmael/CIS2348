#Ismael Diaz (PSID: 1846093)
#CIS 2348 Homework #1 Zylabs 1.20

ljuice = float(input("Enter amount of lemon juice (in cups):\n"))
water = float(input("Enter amount of water (in cups):\n"))
anectar = float(input("Enter amount of agave nectar (in cups):\n"))
servings = float(input("How many servings does this make\n"))
print()

print("Lemonade ingredients - yields", "{:.2f}".format(servings), "servings")
print("{:.2f}".format(ljuice), "cup(s) lemon juice")
print("{:.2f}".format(water), "cup(s) water")
print("{:.2f}".format(anectar), "cup(s) agave nectar")
print()

servings = float(input("How many servings would you like to make?\n"))
print()
print("Lemonade ingredients - yields", "{:.2f}".format(servings), "servings")
print("{:.2f}".format(ljuice*servings), "cup(s) lemon juice")
print("{:.2f}".format(water*servings), "cup(s) water")
print("{:.2f}".format(anectar*servings), "cup(s) agave nectar")
print()
print("Lemonade ingredients - yields", "{:.2f}".format(servings), "servings")
print("{:.2f}".format((ljuice*servings)/16), "gallon(s) lemon juice")
print("{:.2f}".format((water*servings)/16), "gallon(s) water")
print("{:.2f}".format((anectar*servings)/16), "gallon(s) agave nectar")