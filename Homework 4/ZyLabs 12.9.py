# Ismael Diaz (PSID: 1846093)
# CIS 2348 Homework #4 ZyLabs 12.9
# Code template received from ZyLabs 12.8

# Split input into 2 parts: name and age
parts = input().split()
name = parts[0]
while name != '-1':
    try:
        age = int(parts[1]) + 1
    except ValueError:
        age = 0

    print('{} {}'.format(name, age))

    # Get next line
    parts = input().split()
    name = parts[0]
