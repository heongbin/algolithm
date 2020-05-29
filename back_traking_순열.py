N , S = map(int,input().split())

m=[0 for _ in range(N)]
m = list(map(int,input().split()))
#visited = [[0 for _ in range(21)] for _ in range(10000001)]
def dfs(start,sums):
    global answer
    if sums==S:
        answer+=1



    for i in range(start,N):
        sums+=m[i]
        dfs(i+1,sums)
        sums-=m[i]

answer=0

sums=0
#visited[0][0]=1
for i in range(N):
    dfs(i+1,m[i])
print(answer)