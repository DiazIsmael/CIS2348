#Ismael Diaz (PSID: 1846093)
#CIS 2348 Homework #2 Zylabs 8.10

raw_word = input()
word = raw_word.replace(" ", "")

i = len(word)

backword = word[i::-1]

if backword == word:
    print(raw_word, "is a palindrome")
else:
    print(raw_word, "is not a palindrome")