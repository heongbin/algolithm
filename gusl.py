#빨간구슬을 구멍에 통과시키기.
N,M = map(int,input().split())
#세로 N  가로 M
m=[]
for i in range(N):
    a=list(str(input()))
    m.append(a)



class Point:
    def __init__(self,rx,ry,bx,by,cnt):
        self.rx=rx
        self.ry=ry
        self.bx=bx
        self.by=by
        self.cnt=cnt




for i in range(N):
    for j in range(M):
        if m[i][j]=='R':
            rx=j
            ry=i

        elif m[i][j]=='B':
            bx=j
            by=i
visited=[[[[0 for _ in range(N)] for _ in range(M)] for _ in range(N)] for _ in range(M)]
#visited[rx][ry][bx][by]

answer=0
point=Point(rx,ry,bx,by,0)
dx=[1,-1,0,0]
dy=[0,0,1,-1]
#오른쪽,왼쪽,아래쪽,위쪽


cnt=0
q=[point]
visited[rx][ry][bx][by]=1
flag=0
while q:
    w=q.pop(0)
    if w.cnt>10:
        answer=-1
        break
    if m[w.ry][w.rx] == 'O':
        flag=1
        answer=w.cnt
        break
    for direc in range(4):
            nrx=w.rx+dx[direc]
            nry=w.ry+dy[direc]
            nbx=w.bx+dx[direc]
            nby=w.by+dy[direc]


            while 1:

                if m[nry][nrx]=="#":
                    nrx-=dx[direc]
                    nry-=dy[direc]
                    break
                elif m[nry][nrx]=="O":
                    break
                nrx+=dx[direc]
                nry+=dy[direc]

            while 1:

                if m[nby][nbx]=="#":
                    nbx-=dx[direc]
                    nby-=dy[direc]
                    break
                elif m[nby][nbx]=='O':
                    break
                nbx+=dx[direc]
                nby+=dy[direc]

            if m[nby][nbx]=="O":
                continue

            #오른,왼,아래,위
            if nbx==nrx and nby==nry:
                if direc==0:
                    if w.rx>w.bx:
                        nbx-=1
                    elif w.rx<w.bx:
                        nrx-=1
                elif direc==1:
                    if w.rx>w.bx:
                        nrx+=1
                    elif w.rx<w.bx:
                        nbx+=1
                elif direc==2:
                    if w.ry>w.by:
                        nby-=1
                    elif w.ry<w.by:
                        nry-=1
                elif direc==3:
                    if w.ry>w.by:
                        nry+=1
                    elif w.ry<w.by:
                        nby+=1

            if visited[nrx][nry][nbx][nby]==0:
                visited[nrx][nry][nbx][nby]=1
                q.append(Point(nrx,nry,nbx,nby,w.cnt+1))








if flag:
    print(answer)
else:
    print(-1)



