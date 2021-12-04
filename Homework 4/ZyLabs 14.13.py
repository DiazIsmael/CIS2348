# Ismael Diaz (PSID: 1846093)
# CIS 2348 Homework #4 ZyLabs 14.13

def partition(usernames, low, high):
    pindex = low + (high - low) // 2
    pivot = usernames[pindex]

    done = False
    l = low
    h = high
    while not done:
        while usernames[l] < pivot:
            l = l + 1
        while pivot < usernames[h]:
            h = h - 1

        if l <= h:
            usernames[l], usernames[h] = usernames[h], usernames[l]

            l = l + 1
            h = h - 1
        else:
            done = True

    return h


def quicksort(usernames, l, h):
    global num_calls
    num_calls += 1

    if l >= h:
        return

    m = partition(usernames, l, h)

    quicksort(usernames, l, m)
    quicksort(usernames, m + 1, h)
    return


if __name__ == "__main__":
    usernames = []
    newID = input()
    num_calls = 0

    while newID != "-1":
        usernames.append(newID)
        newID = input()

    quicksort(usernames, 0, len(usernames)-1)
    print(num_calls)
    for user in usernames:
        print(user)