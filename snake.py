
def dfs(x,y,direc,idx,time):
    global m
    global snake_length
    global flag
    while True:
        print([x,y])
        print(snake_length)
        time+=1
        x=x+dx[direc]
        y=y+dy[direc]
        if x<0 or x>=N or y<0 or y>=N or m[y][x]==2:
            x-=dx[direc]
            y-=dy[direc]
            time-=1
            flag=1
            break

        snake_length.append([y,x])

        if m[y][x]!=1:
            tmp=snake_length.pop(0) #꼬리부분
            m[tmp[0]][tmp[1]]=0
            m[y][x]=2
        elif m[y][x]==1:
            m[y][x]=2


        if time==snake[idx][0]:
            if snake[idx][1]=="L":
                direc=((direc+1)%4+2)%4
            elif snake[idx][1]=="D":
                direc=(direc+1)%4

            idx += 1  # 다음 회전 방향을 표시
        if idx>=L:
            idx-=1

    if flag==1:
        return time


N = int(input())
m=[[0 for _ in range(N)] for _ in range(N)]

K = int(input())
apple = [[0 for _ in range(2)] for _ in range(K)]

for i in range(K):
    apple[i][0], apple[i][1] = map(int, input().split())


L = int(input())

snake=[["" for _ in range(2)] for _ in range(L)]
for i in range(L):
    snake[i][0], snake[i][1] = map(str,input().split())
    snake[i][0]=int(snake[i][0])


for i in range(len(apple)):
    m[apple[i][0]-1][apple[i][1]-1]=1







dx=[0,1,0,-1]
dy=[-1,0,1,0]
#위, 오른,아래,왼



x=0
y=0

snake_length=[[0,0]]
m[0][0]=2


#뱀은 2 사과는 1
flag=0

print(dfs(0,0,1,0,0))