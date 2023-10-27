word = input().lower()
liczba = len(word)
listWord = list(word)

newLista = []
for char in listWord:
    if char != "a" and char != "y" and char != "e" and char != "u" and char != "i" and char != "o":
        newLista.append(".")
        newLista.append(char)



print(''.join(newLista))


