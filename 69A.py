liczbaWierszy = int(input())
wektorA = 0
wektorB = 0
wektorC = 0
tabela = []
#for _ in range(liczbaWierszy):
#    tabela.append([0] * 3)

for i in range(liczbaWierszy):
    a,b,c = map(int, input().split())
    tabela.append([a,b,c])

for i in range(liczbaWierszy):
    wektorA = tabela[i][0] + wektorA
    wektorB = tabela[i][1] + wektorB
    wektorC = tabela[i][2] + wektorC

if wektorA == 0 and wektorB == 0 and wektorC == 0:
    print("YES")
else:
    print("NO")
