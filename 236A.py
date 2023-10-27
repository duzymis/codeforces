nick = str(input())
newWord = ''.join(set(nick))

if len(newWord)%2 == 0:
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')