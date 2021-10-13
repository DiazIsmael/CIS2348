#Ismael Diaz (PSID: 1846093)
#CIS 2348 Homework #2 Zylabs 7.25

def exact_change(user_total):
    dollars = user_total // 100
    rem = user_total % 100

    quarters = rem // 25
    rem = rem % 25

    dimes = rem // 10
    rem = rem % 10

    nickels = rem // 5
    rem = rem % 5

    pennies = rem // 1
    return dollars, quarters, dimes, nickels, pennies

if __name__ == "__main__":
    input_val = int(input())
    num_dollars, num_quarters, num_dimes, num_nickels, num_pennies = exact_change(input_val)

    if input_val <= 0:
        print("no change")
    else:
        if num_dollars > 1:
            print(num_dollars, "dollars")
        elif num_dollars == 1:
            print(num_dollars, "dollar")

        if num_quarters > 1:
            print(num_quarters, "quarters")
        elif num_quarters == 1:
            print(num_quarters, "quarter")

        if num_dimes > 1:
            print(num_dimes, "dimes")
        elif num_dimes == 1:
            print(num_dollars, "dime")

        if num_nickels > 1:
            print(num_nickels, "nickels")
        elif num_nickels == 1:
            print(num_nickels, "nickel")

        if num_pennies > 1:
            print(num_pennies, "pennies")
        elif num_pennies == 1:
            print(num_pennies, "penny")