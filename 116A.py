
x = int(input())

max = 0
liczbaPasazerow = 0
for i in range(x):
    wysiada, wsiada = map(int, input().split())
    liczbaPasazerow = liczbaPasazerow + wsiada - wysiada
    print(liczbaPasazerow)
    if max < liczbaPasazerow:
        max = liczbaPasazerow

print(liczbaPasazerow)