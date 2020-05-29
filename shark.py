#N*N크기  아기상어 1마리

#아기상어의 크기 2

#아기상어의 크기<큰물고기는 지나갈수X,먹을수X

#아기상어와 크기가 같은 물고기는 지나갈수 O,  먹을수X

#물고기는 가장 가까운 물고기를 먹는다

#위에 물고기를 먼저먹고, 왼쪽을 물고기를 우선순위로
dx=[1,-1,0,0]
dy=[0,0,1,-1]

N=int(input())
m=[[0 for _ in range(N)] for _ in range(N)]


for i in range(N):
    m[i]=list(map(int,input().split()))



for i in range(N):
    for j in range(N):
        if m[i][j]==9:
            startx=j
            starty=i
            m[i][j]=0

class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y





def checkRange(x,y):
    if x<0 or x>=N or y<0 or y>=N:
        return False
    return True



max_value=1000000
answer=0
sharksize=2
sizecnt=0
time=0
while True:
    distance = [[-1 for _ in range(N)] for _ in range(N)]
    q=[]
    distance[starty][startx]=0
    q=[Point(startx,starty)]
    mini_dist=max_value
    mini_x=max_value
    mini_y=max_value

    while q:
        shark=q.pop(0)
        x=shark.x
        y=shark.y
        for direc in range(4):
            nx=x+dx[direc]
            ny=y+dy[direc]
            if checkRange(nx,ny)==False:
                continue
            if sharksize<m[ny][nx] or distance[ny][nx]>-1:
                continue

            distance[ny][nx]=distance[y][x]+1

            if sharksize>m[ny][nx] and m[ny][nx]!=0:
                if mini_dist>distance[ny][nx]:
                    mini_x=nx
                    mini_y=ny
                    mini_dist=distance[ny][nx]
                elif mini_dist==distance[ny][nx]:
                    if mini_y>ny:
                        mini_x=nx
                        mini_y=ny

                    elif mini_y==ny:
                        if mini_x>nx:
                            mini_x=nx
                            mini_y=ny

            q.append(Point(nx,ny))


    if mini_x<max_value and mini_y<max_value:
        answer+=distance[mini_y][mini_x]
        sizecnt+=1

        if sharksize==sizecnt:
            sharksize+=1
            sizecnt=0

        m[mini_y][mini_x]=0

        startx=mini_x
        starty=mini_y
    else:
        break

















print(answer)