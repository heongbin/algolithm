from collections import deque

#지도의 가로, 세로 길이 N,M   R,C좌표 명령개수
N,M,R,C,K=map(int,input().split())
m=[[0 for _ in range(M)] for i in range(N)]
for i in range(N):
    m[i]=list(map(int,input().split()))  #R.C
#1동2서3북4남
direc=[0 for i in range(K)]
direc=list(map(int,input().split()))
#주사위는 모든면이 0으로.
#r은 북으로부터의 거리, c는 서로부터의 거리
dr=[0,0,-1,1]
dc=[1,-1,0,0]
#이동할떄마다 주사위의 윗면에 쓰여잇는 칸의 수를 출력. answer
dqhor=deque([0,0,0,0]) #동쪽이나 서쪽으로 주사위를 이동시킬때
#[바닥면,동쪽면,윗면,서쪽면]
dqver=deque([0,0,0,0]) #북쪽이나 남쪽으로 이동할떄
#[바닥면,북쪽면,윗면,남쪽면]


def move(r,c,direc,dqhor,dqver):
    global m
    if direc==1:#동쪽
        if 0 <= r + dr[direc - 1] and r + dr[direc - 1] <= len(m) - 1 and 0 <= c + dc[direc - 1] and c + dc[direc - 1] <= len(m[0]) - 1:
            dqhor.rotate(-1)
            if m[r+dr[direc-1]][c+dc[direc-1]]!=0: #지도에 써있는 칸의 숫자가 0이 x면, 지도의칸숫자가 바닥면에 복사 그리고 그 칸은 0
                dqhor[0]=m[r+dr[direc-1]][c+dc[direc-1]]
                m[r+dr[direc-1]][c+dc[direc-1]]=0

            elif m[r+dr[direc-1]][c+dc[direc-1]]==0:  #지도에 써잇는 칸의 숫자가 0이면:주사위의 바닥면을 그바닥에 복사
                m[r + dr[direc - 1]][c + dc[direc - 1]]=dqhor[0]

            dqver[0], dqver[2] = dqhor[0], dqhor[2]


    elif direc==2: #서쪽
        if 0<=r+dr[direc-1] and r+dr[direc-1]<=len(m)-1 and  0<=c+dc[direc-1] and c+dc[direc-1]<=len(m[0])-1:
            dqhor.rotate(1)
            if m[r+dr[direc-1]][c+dc[direc-1]]!=0: #지도에 써있는 칸의 숫자가 0이 x면, 지도의칸숫자가 바닥면에 복사 그리고 그 칸은 0
                dqhor[0]=m[r+dr[direc-1]][c+dc[direc-1]]
                m[r+dr[direc-1]][c+dc[direc-1]]=0

            elif m[r+dr[direc-1]][c+dc[direc-1]]==0:  #지도에 써잇는 칸의 숫자가 0이면:주사위의 바닥면을 그바닥에 복사
                m[r + dr[direc - 1]][c + dc[direc - 1]]=dqhor[0]

            dqver[0], dqver[2] = dqhor[0], dqhor[2]



    elif direc == 3:  # 북쪽
        if 0 <= r + dr[direc - 1] and r + dr[direc - 1] <= len(m) - 1 and 0 <= c + dc[direc - 1] and c + dc[direc - 1] <= len(m[0]) - 1:
            dqver.rotate(-1)
            if m[r + dr[direc - 1]][c + dc[direc - 1]] != 0:  # 지도에 써있는 칸의 숫자가 0이 x면, 지도의칸숫자가 바닥면에 복사 그리고 그 칸은 0
                dqver[0] = m[r + dr[direc - 1]][c + dc[direc - 1]]
                m[r + dr[direc - 1]][c + dc[direc - 1]] = 0
            elif m[r + dr[direc - 1]][c + dc[direc - 1]] == 0:  # 지도에 써잇는 칸의 숫자가 0이면:주사위의 바닥면을 그바닥에 복사
                m[r + dr[direc - 1]][c + dc[direc - 1]] = dqver[0]

            dqhor[0],dqhor[2]=dqver[0],dqver[2]

    elif direc == 4:  # 남쪽
        if 0 <= r + dr[direc - 1] and r + dr[direc - 1] <= len(m) - 1 and 0 <= c + dc[direc - 1] and c + dc[direc - 1] <= len(m[0]) - 1:
            dqver.rotate(1)
            if m[r + dr[direc - 1]][c + dc[direc - 1]] != 0:  # 지도에 써있는 칸의 숫자가 0이 x면, 지도의칸숫자가 바닥면에 복사 그리고 그 칸은 0
                dqver[0] = m[r + dr[direc - 1]][c + dc[direc - 1]]
                m[r + dr[direc - 1]][c + dc[direc - 1]] = 0
            elif m[r + dr[direc - 1]][c + dc[direc - 1]] == 0:  # 지도에 써잇는 칸의 숫자가 0이면:주사위의 바닥면을 그바닥에 복사
                m[r + dr[direc - 1]][c + dc[direc - 1]] = dqver[0]

            dqhor[0], dqhor[2] = dqver[0], dqver[2]
    return


flag=0

for i in range(len(direc)):
    if 0 <= R + dr[direc[i] - 1] and R + dr[direc[i] - 1] <= len(m) - 1 and 0 <= C + dc[direc[i] - 1] and C + dc[direc[i] - 1] <= len(m[0]) - 1:
        move(R,C,direc[i],dqhor,dqver)
        print(dqver[2])
        R += dr[direc[i] - 1]
        C += dc[direc[i] - 1]
    else:
        continue



