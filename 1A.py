import math

# Wczytaj dane wejściowe
n, m, a = map(int, input().split())

# Oblicz minimalną liczbę kamieni
kamienie_poziomo = math.ceil(n / a)
kamienie_pionowo = math.ceil(m / a)

# Oblicz całkowitą liczbę kamieni potrzebną do pokrycia placu
wynik = kamienie_poziomo * kamienie_pionowo

# Wyświetl wynik
print(wynik)
