n, k = map(int, input().split())
scores = list(map(int, input().split()))

# Wynik początkowy
wynik = 0

# Obliczenia
for score in scores:
    if score > 0 and score >= scores[k - 1]:
        wynik += 1

# Wyświetl wynik
print(wynik)
