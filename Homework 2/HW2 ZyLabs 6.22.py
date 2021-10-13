#Ismael Diaz (PSID: 1846093)
#CIS 2348 Homework #2 Zylabs 6.22

x1 = int(input())
y1 = int(input())
ans1 = int(input())
x2 = int(input())
y2 = int(input())
ans2 = int(input())

xsolution = int
ysolution = int

for x in range(-10, 11):
    for y in range(-10, 11):
        if (x1 * x) + (y1 * y) == ans1 and (x2 * x) + (y2 * y) == ans2:
            xsolution = x
            ysolution = y
            print(xsolution, ysolution)
            exit()

print("No solution")
