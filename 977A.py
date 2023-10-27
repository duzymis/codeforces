liczba,operacje = map(int, input())
for i in range(operacje):
    if liczba == 1:
        print("1")
        break
    elif liczba % 10 ==0:
        liczba = liczba // 10
    elif liczba % 10 !=0:
        liczba = liczba - 1


print("Wynik:",liczba)