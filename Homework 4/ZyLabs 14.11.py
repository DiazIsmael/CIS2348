# Ismael Diaz (PSID: 1846093)
# CIS 2348 Homework #4 ZyLabs 14.11

def selection_sort_descend_trace(list):
    for i in range(len(list)-1):
        temp = i
        #print("i:", i)
        for num in range(i+1, len(list)):
            #print("num:", num)
            if list[temp] < list[num]:
                temp = num

        list[i], list[temp] = list[temp], list[i]
        for j in list:
            print(j, end=' ')
        print()


if __name__ == "__main__":
    rawlist = input()
    rawlist = rawlist.split()
    numlist = []

    for num in rawlist:
        numlist.append(int(num))

    selection_sort_descend_trace(numlist)
