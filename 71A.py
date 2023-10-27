liczba = input()
liczba = int(liczba)

for i in range(liczba):
    word = input()
    if len(word) < 11:
        print(word)
    else:
        newWord = word[0]
        char = len(word)-2
        char = str(char)
        newWord = newWord + char + word[len(word)-1]
        print(newWord)