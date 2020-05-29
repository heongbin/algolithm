import copy
from collections import deque

class Data:
    def __init__(self,x,y,number,time):
        self.x=x
        self.y=y
        self.check=False #체크여부
        self.number=number
        self.time=time


dx=[0,0,1,-1]
dy=[1,-1,0,0]




def checkRange(x,y):
    if x<0 or x>=N or y<0 or y>=N:
        return False

    return True

def Spread_v(v_nums):
    copy_m=copy.deepcopy(m)
    tmp_v=deque()
    chekc_v=deque()

    for i in range(len(v)):
        if v[i].check==True:
           copy_m[v[i].y][v[i].x]=v[i].number
           tmp_v.append(v[i])
           chekc_v.append(v[i])
        else:
            copy_m[v[i].y][v[i].x]=0

    max_len=0
    while tmp_v:
        tmpv=tmp_v.popleft()
        x=tmpv.x
        y=tmpv.y
        t=tmpv.time
        cx=0
        cy=0

        flag=0
        for j in range(4):
            nx=x+dx[j]
            ny=y+dy[j]
            if checkRange(nx,ny)==False:
                continue
            if copy_m[ny][nx]!=0:
                continue
            if copy_m[ny][nx]==0 and m[ny][nx]==2: #비활성화 바이러면
                flag=1
                copy_m[ny][nx]=tmpv.number
                v_nums-=1
                tmp_v.append(Data(nx,ny,tmpv.number,t+1))
                continue
            flag=1
            copy_m[ny][nx]=tmpv.number
            v_nums-=1
            max_len=max(max_len,t+1)
            if min_time<=t+1:
                return min_time
            tmp_v.append(Data(nx,ny,tmpv.number,t+1))



    if v_nums!=0:
        return 1000000



    return max_len









def dfs(start,cnt):
    global min_time
    global v
    if cnt==M:
        min_time=min(min_time,Spread_v(v_nums))
        return

    for i in range(start,len(v)):
        if v[i].check==False:
            v[i].check=True
            dfs(i,cnt+1)
            v[i].check=False



min_time=1000000
N,M = map(int,input().split())
v_nums=N*N-M
m=[[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    m[i]=list(map(int,input().split()))

#M<=2의개수 <=10

#위치를 담는 배열을 만듬.
v=deque()

v_number=2
for i in range(N):
    for j in range(N):
        if m[i][j]==2:
            v.append(Data(j,i,v_number,0))
            v_number+=1
        if m[i][j]==1:
            v_nums-=1


dfs(0,0)
if min_time==1000000:
    min_time=-1
print(min_time)