year = int(input())


def duplicates(s):
    s = str(s)
    a1 = s.count(s[0])
    a2 = s.count(s[1])
    a3 = s.count(s[2])
    a4 = s.count(s[3])

    if a1 == 1 and a2 == 1 and a3 == 1 and a4 == 1:
        return "Y"
    else:
        return "F"


while True:
    year = year + 1
    if duplicates(year) == "Y":
        print(year)
        break


