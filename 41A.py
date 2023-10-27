word1 = str(input())
word2 = str(input())


if word1 == word2[::-1]:
    print("YES")
else:
    print("NO")