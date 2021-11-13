#Ismael Diaz (PSID: 1846093)
#CIS 2348 Homework #3 Zylabs 11.27

def menu():
    print("\nMENU")
    print("a - Add player")
    print("d - Remove player")
    print("u - Update player rating")
    print("r - Output players above a rating")
    print("o - Output roster")
    print("q - Quit")
    print()

def addPlayer(roster):
    jersey = int(input("\nEnter player jersey number:"))
    rating = int(input("Enter player rating:"))
    roster[jersey] = rating

def outputRoster(roster):
    print("ROSTER")

    sortedRoster = sorted(roster.keys())

    for jersey in sortedRoster:
        print("Jersey number: {}, Rating: {}".format(jersey, roster[jersey]))

def deletePlayer(roster):
    jersey = int(input("\nEnter player jersey number:"))

    if jersey not in roster.keys():
        pass
    else:
        del roster[jersey]

def updatePlayer(roster):
    jersey = int(input("\nEnter player jersey number:"))

    if jersey not in roster.keys():
        pass
    else:
        rating = int(input("\nEnter player rating:"))
        roster[jersey] = rating


def aboveRating(roster):
    rating = int(input("\nEnter a rating:"))
    print("ABOVE", rating)

    sortedRoster = sorted(roster.keys())

    for jersey in sortedRoster:
        if roster[jersey] > rating:
            print("Jersey number: {}, Rating: {}".format(jersey, roster[jersey]))


if __name__ == "__main__":
    roster = {}
    i = 1

    for i in range(0, 5):
        jersey = int(input("Enter player " + str(i + 1) + "'s jersey number:\n"))
        rating = int(input("Enter player " + str(i + 1) + "'s rating:\n"))
        print()

        roster[jersey] = rating
    outputRoster(roster)

    while True:
        menu()
        option = input("Choose an option:\n")

        if option == 'a':
            addPlayer(roster)
        elif option == 'd':
            deletePlayer(roster)
        elif option == 'o':
            outputRoster(roster)
        elif option == 'u':
            updatePlayer(roster)
        elif option == 'r':
            aboveRating(roster)
        elif option == 'q':
            break
