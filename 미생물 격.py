class Insect:
    def __init__(self,idx,x,y,number,direc):
        self.idx=idx
        self.x=x
        self.y=y
        self.direc=direc #미생물의 현 방향
        self.number=number
        self.live=True


def check_range(x,y):
    if x<=0 or y<=0 or x>=N-1 or y>=N-1:
        return False
    return True

dx=[0,0,-1,1]
dy=[-1,1,0,0]

#상,하,좌,우
T=int(input())
for test_case in range(1,T+1):
    N,M,K = map(int,input().split())
    #N은 MAP의 크기, M시간후의 답, K는 미생문 집단 개수.

    insect_list=[]
    m=[[[] for _ in range(N)] for _ in range(N)] #각맵마다 어떤 샐물이 있는지 표시.
    for i in range(K):
        y,x,number,direc = map(int,input().split())
        insect_list.append(Insect(i,x,y,number,direc-1))
        m[y][x].append(i)


    t=0
    while True:
        if t==M:
            break

        for i in range(K): #각 미생물당
            if insect_list[i].live==True:
                idx=insect_list[i].idx
                x=insect_list[i].x
                y=insect_list[i].y
                number=insect_list[i].number
                direc=insect_list[i].direc
                nx=x+dx[direc]
                ny=y+dy[direc]
                print([x,y])
                if check_range(nx,ny)==False: #경게에 닿으면
                    insect_list[i].number=number//2
                    if insect_list[i].number==0:
                        insect_list[i].live=False

                    if direc==2:
                        direc=3
                    elif direc==3:
                        direc=2
                    elif direc==0:
                        direc=1
                    else:
                        direc=0

                m[y][x].remove(idx)
                if insect_list[i].live==True:
                    m[ny][nx].append(idx)
                    insect_list[i].x=nx
                    insect_list[i].y=ny
                    insect_list[i].direc=direc



        for i in range(N):
            for j in range(N):
                if len(m[i][j])>=2: #생물들이 만낫다면.
                    max_num = 0  # 해당 구역의 최대 생물수.
                    max_idx = 0  # 그 생물의 번호.
                    sums = 0
                    for k in range(len(m[i][j])):
                        sums+=insect_list[m[i][j][k]].number
                        if max_num<insect_list[m[i][j][k]].number:
                            max_num=insect_list[m[i][j][k]].number
                            max_idx=m[i][j][k]

                    for k in range(len(m[i][j])):
                        if m[i][j][k]!=max_idx:
                            insect_list[m[i][j][k]].live=False

                    m[i][j]=[max_idx]
                    insect_list[max_idx].number=sums


        t+=1


    answer=0
    for i in range(len(insect_list)):
        if insect_list[i].live==True:
            answer+=insect_list[i].number


    print("#{} {}".format(test_case,answer))












