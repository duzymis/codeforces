liczbaGier,mecze = map(input().split())


A = mecze.count("A")
D = mecze.count("D")
if A > D:
    print("Anton")
elif A < D:
    print("Danik")
else:
    print("Friendship")