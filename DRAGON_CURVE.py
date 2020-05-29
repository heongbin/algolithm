#표시할 드래곤 커브의 개수 N
N=int(input())

# x y d g : x y좌표 d는 방향 (0: 오른쪽 , 1; 위 , 2: 왼쪽 3:아래), g는 세대

dragons=[[0 for _ in range(4)] for _ in range(N)]



def rangecheck(x,y):
    if x<0 or x>=101 or y<0 or y>=101:
        return False
    return True

dx=[1,0,-1,0]
dy=[0,-1,0,1]

for i in range(N):
    dragons[i]=list(map(int,input().split()))


visited=[[0 for _ in range(101)] for _ in range(101)]

answer=0
for dragon in dragons:
    x=dragon[0]
    y=dragon[1]
    direc=dragon[2]
    g=dragon[3]

    visited[y][x]=1
    direclist=[direc]
    #d를 list로
    for i in range(g):
        for j in range(len(direclist)-1,-1,-1):
            direclist.append((direclist[j]+1)%4)

    for i in direclist:
        x=x+dx[i]
        y=y+dy[i]

        visited[y][x]=1


for i in range(101):
    for j in range(101):
        if visited[i][j]==1 and visited[i+1][j]==1 and visited[i][j+1]==1 and visited[i+1][j+1]==1 and i+1<=100 and j+1<=100:
            answer+=1


print(answer)














