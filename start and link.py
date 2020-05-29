N=int(input())
m=[[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    m[i]=list(map(int,input().split()))


# N/2씩 N명중에서

check=[0 for _ in range(N)]


def divide_team_andsum(): #각팀원들을 나눔.
    teamA=[]
    teamB=[]
    for i in range(N):
        if check[i]==1:
            teamA.append(i)
        else:
            teamB.append(i)
    sumsA=0
    for i in range(N//2):
        for j in range(i+1,N//2):
            sumsA+=m[teamA[i]][teamA[j]]+m[teamA[j]][teamA[i]]

    sumsB=0
    for i in range(N//2):
        for j in range(i+1,N//2):
            sumsB+=m[teamB[i]][teamB[j]]+m[teamB[j]][teamB[i]]

    return abs(sumsB-sumsA)



def permutation(start,cnt):
    global MinNumber
    global check

    if cnt==N/2: #check 0 과 check 1로 팀이 나뉨.
        MinNumber=min(MinNumber,divide_team_andsum())
        return
#1 3 4 , 2 4 6 이 팀이 되어있다면

    for i in range(start,N):
        if check[i]!=1:
            check[i]=1
            permutation(i,cnt+1)
            check[i]=0

MinNumber=1000000
permutation(0,0)

print(MinNumber)




