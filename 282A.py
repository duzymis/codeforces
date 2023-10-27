liczba = int(input())
x = 0
task = []

for i in range(liczba):
    task.append(input())

for i in range(liczba):
    if task[i] == "X++" or task[i] == "++X":
        x=x+1
    elif task[i] == "--X" or task[i] == "X--":
        x=x-1;
print(x)