countFriends,height = map(int,input().split())
list = str(input())
newList = list.split(" ")
road = 0
for i in range(countFriends):


    if height < int(newList[i]):

        road=road+2
    else:
        road=road+1


print(road)