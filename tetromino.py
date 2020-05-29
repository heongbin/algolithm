#N,M
N,M=map(int,input().split())
m=[[0 for _ in range(M)] for _ in range(N)]
for i in range(N):
    m[i]=list(map(int,input().split()))

visited=[[0 for _ in range(M)] for _ in range(N)]

dx=[-1,1,0,0]
dy=[0,0,1,-1]

answer=0

def RangCheck(x,y):
    if x<0 or x>=M or y>=N or y<0:
        return False
    return True

def dfs(x,y,cnt,sums):
    global answer
    if cnt==3:
        if answer<sums:
            answer=sums
            return
        return

    for direc in range(4):
        nx=x+dx[direc]
        ny=y+dy[direc]
        if RangCheck(nx,ny)==False:
            continue

        if visited[ny][nx]==0:
            sums+=m[ny][nx]
            visited[ny][nx]=1
            dfs(nx,ny,cnt+1,sums)
            sums-=m[ny][nx]
            visited[ny][nx]=0


for i in range(N):
    for j in range(M):
        visited[i][j]=1
        dfs(j,i,0,m[i][j])
        visited[i][j]=0


othersums=0

for i in range(N): #ㅜ
    for j in range(M):
        if  i+1<N and j+2<M:
            othersums=m[i][j]+m[i][j+1]+m[i][j+2]+m[i+1][j+1]
            answer=max(othersums,answer)

for i in range(N): #ㅗ
    for j in range(M):
        if  i-1>=0 and j+2<M:
            othersums=m[i][j]+m[i][j+1]+m[i][j+2]+m[i-1][j+1]
            answer=max(othersums,answer)

for i in range(N): #ㅏ
    for j in range(M):
        if i+2<N and j+1<M:
            othersums=m[i][j]+m[i+1][j]+m[i+2][j]+m[i+1][j+1]
            answer=max(othersums,answer)

for i in range(N): #ㅓ
    for j in range(M):
        if i+2<N and j-1>=0:
            othersums=m[i][j]+m[i+1][j]+m[i+2][j]+m[i+1][j-1]
            answer=max(othersums,answer)

print(answer)
