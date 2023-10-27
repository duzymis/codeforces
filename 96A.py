liczba = str(input())
licznik = 0

for i in range(len(liczba)-1):
    if liczba[i] == liczba[i+1]:
        licznik += 1
        if licznik == 7:
            print("YES")
            break
    else:
        licznik = 1

if licznik != 7:
    print("NO")
