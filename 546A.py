cenaBananna, iloscPieniedzy, liczbaBananow = map(int, input().split())

kwota = 0
for i in range(liczbaBananow):
    kwota = kwota + (i+1)*cenaBananna


pozyczka = kwota-iloscPieniedzy

if pozyczka < 0:
    print(0)
else:
    print(pozyczka)