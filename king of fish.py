
R,C,M = map(int,input().split())

shark=[[0 for _ in range(5)] for _ in range(M)]
for i in range(M):
    shark[i]=list(map(int,input().split()))




class SharkData:
    def __init__(self, name, x, y, speed, direction, size,live):
        self.name = name
        self.x = x
        self.y = y
        self.speed = speed
        self.direction = direction
        self.size = size
        self.live=live

def checkrange(x,y):
    if x<0 or x>=C or y<0 or y>=R:
        return False
    return True








m=[[0 for _ in range(C)] for _ in range(R)]




sharklist=[]
for i in range(M): #인덱스는 shark의 순서, value는 m에 표시된 값
    sharklist.append(SharkData(i+1,shark[i][1]-1,shark[i][0]-1,shark[i][2],shark[i][3]-1,shark[i][4],1))
# [0:1, 1:2]
dx=[0,0,1,-1]
dy=[-1,1,0,0]

#r c 상어의 위치 s 속력  d 이동방향 z 크기

#d 1 위 2  아래 3 오른 4 왼

for i in range(len(sharklist)):
    m[sharklist[i].y][sharklist[i].x]=sharklist[i].name #상어 위치 m에 표시



sizesum=0



for i in range(C):
    tmpshark=0
    for j in range(R):
        if m[j][i]!=0:
            tmpshark=m[j][i]
            break


    if tmpshark!=0 and sharklist:
        for j in range(len(sharklist)):
            if sharklist[j].name==tmpshark: #상어 업데이트
                sizesum+=sharklist[j].size
                m[sharklist[j].y][sharklist[j].x]=0
                sharklist[j].live=0
                break



    for j in range(len(sharklist)): #남아있는 상어들 정보
        if sharklist[j].live==0 or sharklist[j].speed==0:
            continue
        ny=sharklist[j].y
        nx=sharklist[j].x
        m[ny][nx]=0

        if sharklist[j].direction==0 or sharklist[j].direction==1:
            sharkspeed=sharklist[j].speed%(R*2-2)
        else:
            sharkspeed=sharklist[j].speed%(C*2-2)

        if sharkspeed==0:
            continue

        for _ in range(sharkspeed): #m에 상어 좌표를 업데이트 해주는 부분.
            nx+=dx[sharklist[j].direction]
            ny+=dy[sharklist[j].direction]

            if checkrange(nx,ny)==False: #경계선에 닿아서 넘어가면
                nx-=dx[sharklist[j].direction]
                ny-=dy[sharklist[j].direction]
                if sharklist[j].direction==0:
                    sharklist[j].direction=1
                elif sharklist[j].direction==1:
                    sharklist[j].direction=0
                elif sharklist[j].direction==2:
                    sharklist[j].direction=3
                elif sharklist[j].direction== 3:
                    sharklist[j].direction=2
                nx+=dx[sharklist[j].direction]
                ny+=dy[sharklist[j].direction]

        sharklist[j].y=ny
        sharklist[j].x=nx

        #일단 상어 정보표시 리스트에 업데이트해줌. m에 업데이트하는건 상어들의 이동이 모두끝나고.

    #이동이 다끝나고
    #keylist=list(dic.keys())
    

    for j in range(len(sharklist)-1):
        if sharklist[j].live==0:
            continue
        for k in range(j+1,len(sharklist)):
            if sharklist[k].live==0:
                continue
            if sharklist[j].x==sharklist[k].x and sharklist[j].y==sharklist[k].y: #상어의 위치가 같으면
                if sharklist[j].size>sharklist[k].size:
                    sharklist[k].live=0
                elif sharklist[j].size<sharklist[k].size:
                    sharklist[j].live=0



    for j in sharklist:
        if j.live==1:
            ny=j.y
            nx=j.x
            m[ny][nx]=j.name




print(sizesum)














