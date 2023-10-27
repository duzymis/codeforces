word = list(str(input()))
male = 0
duze = 0
for i in range(len(word)):
    if word[i].islower():
        male=male+1
    else:
        duze=duze+1

if male == duze or male > duze:
    print("".join(word).lower())
else:
    print("".join(word).upper())