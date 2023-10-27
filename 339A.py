task = input()
newList = []
newWord = ""
for i in range(len(task)):
    if task[i] != "+":
        newList.append(task[i])
newList = sorted(newList)

for i in range(len(newList)):
    newWord = newWord + str(newList[i] + "+")
print(newWord[:-1])