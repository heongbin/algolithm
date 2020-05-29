


dx=[-1,1,0,0]
dy=[0,0,-1,1]

T=int(input())
for test_case in range(1,T+1):
    check=0
    q=[[] for _ in range(11)]
    m=[[[0 for _ in range(2)] for _ in range(300)] for _ in range(300)]
    N,M,K =map(int,input().split())
    tmp=[[0 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        tmp[i]=list(map(int,input().split()))



    for i in range(N):
        for j in range(M):
            if tmp[i][j]!=0:
                m[i+150][j+150][0]=tmp[i][j] #맵 각각 구역당 0에는 생명력을
                m[i+150][j+150][1]=tmp[i][j]*2 #그 생명력을 실시간으로 변화시켜주는 변수.
                q[tmp[i][j]].append([j+499,i+499])

    for k in range(K):
        for i in range(10,0,-1):
            length=len(q[i])
            for j in range(length):
                curr=q[i].pop(0)
                x=curr[0]
                y=curr[1]

                m[y][x][1]-=1
                if m[y][x][1]<m[y][x][0]: #활성화된후 처음 복제.
                    for t in range(4):
                        nx=x+dx[t]
                        ny=y+dy[t]
                        if m[ny][nx][0]==0:
                            m[ny][nx][0]=m[y][x][0]
                            m[ny][nx][1]=m[y][x][0]*2
                            q[i].append([nx,ny])


                if m[y][x][1]>0: # 활성화상태이고 살아있다면
                    q[i].append([x,y])




    cnt=0
    for i in range(len(q)):
        print(len(q[i]))
        cnt+=len(q[i])

    print("#{} {}".format(test_case,cnt))


















