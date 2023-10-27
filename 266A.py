liczba = int(input())
word = str(input())

word = list(word)
licz= 0
for i in range(liczba-1):
    if word[i] == word[i+1]:
        licz=licz+1

print(licz)