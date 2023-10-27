wynik = 0
liczba = int(input())
for i in range(liczba):
    a,b,c = map(int, input().split())
    if a+b+c > 1:
        wynik = wynik + 1

print(wynik)