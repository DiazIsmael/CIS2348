#Ismael Diaz (PSID: 1846093)
#CIS 2348 Homework #1 Zylabs 5.22

menu = {"Oil change":35,"Tire rotation":19,"Car wash":7, "Car wax":12}

print("Davy's auto shop services")
print("Oil change -- $35")
print("Tire rotation -- $19")
print("Car wash -- $7")
print("Car wax -- $12")
print()

service1 = input("Select first service:\n")
service2 = input("Select second service:\n")
print()

print("Davy's auto shop invoice")
print()
if service1 == "-":
    print("Service 1: No service")
    print("Service 2: %s," %service2, "$%d" %(menu[service2]))
    print()
    print("Total: $%d" % (menu[service2]))
elif service2 == "-":
    print("Service 1: %s," %service1, "$%d" % (menu[service1]))
    print("Service 2: No service")
    print()
    print("Total: $%d" % (menu[service1]))
else:
    print("Service 1: %s," %service1, "$%d" % (menu[service1]))
    print("Service 2: %s," %service2, "$%d" %(menu[service2]))
    print()
    print("Total: $%d" % (menu[service1] + menu[service2]))
