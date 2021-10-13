#Ismael Diaz (PSID: 1846093)
#CIS 2348 Homework #1 Zylabs 3.19
import math

wheight = int(input("Enter wall height (feet):\n"))
wwidth = int(input("Enter wall width (feet):\n"))
print("Wall area:", wheight*wwidth, "square feet")

paintgal = (wheight*wwidth)/350
print("Paint needed:", '{:.2f}'.format(paintgal), "gallons")
print("Cans needed:", math.ceil(paintgal), "can(s)")
print()

colorchoice = input("Choose a color to paint the wall:\n")
prices = {"red":35,"blue":25,"green":23}
print("Cost of purchasing", colorchoice, "paint: $%d" %(prices[colorchoice]*math.ceil(paintgal)))
