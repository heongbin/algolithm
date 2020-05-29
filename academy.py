import copy

class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y




dx=[-1,1,0,0]
dy=[0,0,-1,1]

def checkrange(x,y):
    if x<0 or x>=C or y<0 or y>=R:
        return False
    return True


def dfs_vi(x,y,after_wall):
    global max_safe

    tmp_q=q[:]

    while tmp_q:
        tmp=tmp_q.pop(0)
        x=tmp.x
        y=tmp.y
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if checkrange(nx,ny)==False:
                continue
            if after_wall[ny][nx]==0:
                after_wall[ny][nx]=2
                tmp_q.append(Point(nx,ny))







def dfs_wall(cnt):
    global max_safe
    global m

    if cnt>=3:
        after_wall=copy.deepcopy(m)


        for i in range(len(q)):
            dfs_vi(q[i].x,q[i].y,after_wall)

        z_cnt=0
        for i in range(R):
            for j in range(C):
                if after_wall[i][j]==0:
                    z_cnt+=1

        max_safe=max(max_safe,z_cnt)
        return


    for i in range(R):
        for j in range(C):
            if m[i][j]==0:
                m[i][j]=1
                dfs_wall(cnt+1)
                m[i][j]=0





max_safe=0

R, C = map(int, input().split())
m = [[0 for _ in range(C)] for _ in range(R)]




for i in range(R):
    m[i] = list(map(int, input().split()))





q=[]

for i in range(R):
    for j in range(C):
        if m[i][j]==2:
            q.append(Point(j,i))






dfs_wall(0)
print(max_safe)

