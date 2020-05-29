#N,M 크기의 맵,
#로봇청소기 방향은 동서남북
#1.현재위치를 청소
#2.현재방향기준, 왼쪽방향부터 탐색.
    #왼쫃방향에 청소가X면, 그방향으로 횐전한다음 한칸전진하고 1번 RE.
    #네방향이 모두청소되어잇다면, 현재방향을 유지한채 뒤로한칸 후진 그리고 2번RE
    #네방향이 모두청소되어잇고 뒤방향이 벽이면 그자리로 스탑.

#세로 N,가로 M
#R,C 로봇청소기의 위치.
#바라보는 방향 d , 북0  동1  남2  서3

N,M=map(int,input().split())
r,c,d = map(int,input().split())
m=[[0 for _ in range(M)] for _ in range(N)]

for i in range(N):
    m[i]=list(map(int,input().split()))



dx=[0,1,0,-1]
dy=[-1,0,1,0]
visited=[[0 for _ in range(M)] for _ in range(N)]

cnt=1

def dfs(x,y,direc):
    global cnt
    global visited

    for i in range(3,-1,-1):
        ndirec=(direc+i)%4
        if m[y+dy[ndirec]][x+dx[ndirec]]==0 and visited[y+dy[ndirec]][x+dx[ndirec]]==0:
            nx=x+dx[ndirec]
            ny=y+dy[ndirec]
            visited[ny][nx]=1
            cnt+=1
            dfs(nx,ny,ndirec)
            return

    x-=dx[direc]
    y-=dy[direc]

    if m[y][x]!=1:
        dfs(x,y,direc)




visited[r][c]=1
dfs(c,r,d)

print(cnt)



