import copy
N= int(input())
m=[[0 for _ in range(N)] for _ in range(N)]
election_sector=copy.deepcopy(m)

for i in range(N):
    m[i]=list(map(int,input().split()))


#d1,d2>=1
#1<=y<y+d1+d2<=N 알아듣기 힘들어 x,y를 바꿧슴. 이거 알아먹는데만 1시간 걸림. 내 돌멍게 대가리
#1<=x-d1<x<x+d2<=N


#5번선거구의 경계선들의 좌표.
#총 4면의 경계선들
#1 (y,x),(y+1,x-1),....,(y+d1,x-d1)
#2 (y,x),(y+1,x+1),....,(y+d2,x+d2)
#3 (y+d1,x-d1),(y+d1+1,x-d1+1),....(y+d1+d2,x-d1+d2)
#4 (y+d2,x+d2),(y+d2+1,x+d2-1),....(y+d2+d1,x+d2-d1)
#결국 34의 도착점은 같음.


#1번선거구 1<=r<y+d1 , 1<=c<=x
#2번선거구 1<=r<=y+d2 , x<c<=N
#3번선거구 y+d1<=r<=N , 1<=c<x-d1+d2
#4번선거구 y+d2<r<=N , x-d1+d2<=x<=N


def checkRange(x,y,d1,d2): #기준점의 범위 초과를 측정하는 함수.
    if 0<=y and y<y+d1+d2 and y+d1+d2<N and 0<=x-d1 and x-d1<x and x<x+d2 and x+d2<N:
        return True
    return False



def make_border(x,y,d1,d2): #5구역의 경계선들을 만드는 함수.
    global five_sector
    five_sector=[]
    copy_map=copy.deepcopy(election_sector)
    find_five=[]


    lsx=x-d1
    lsy=y+d1
    rsx=x+d2
    rsy=y+d2

    #각 꼭지점들의 좌표.
    five_sector.append([x,y])
    find_five.append([x,y])

    five_sector.append([lsx,lsy])

    five_sector.append([rsx,rsy])

    five_sector.append([x-d1+d2,y+d1+d2])


    for i in range(1,d1):
        lx=x-i
        ly=y+i
        find_five.append([lx,ly])
        rrx = rsx - i
        rry = rsy + i
        five_sector.append([lx,ly])
        five_sector.append([rrx,rry])


    for j in range(1,d2):
        rx=x+j
        ry=y+j
        find_five.append([rx,ry])
        llx = lsx + j
        lly = lsy + j
        five_sector.append([rx,ry])
        five_sector.append([llx,lly])

    for i in range(len(five_sector)):
        copy_map[five_sector[i][1]][five_sector[i][0]]=5




    for i in range(len(find_five)):#5번선거구 채우기 함수
        tmpx = find_five[i][0]
        tmpy = find_five[i][1]
        while True:
            nx=tmpx
            tmpy+=1
            if copy_map[tmpy][nx]==0:
                copy_map[tmpy][nx]=5
            else:
                break
    tmp_count_list=[]
    cnt=0
    for i in range(N):
        for j in range(N):
            if copy_map[i][j]==5:
                cnt+=m[i][j]
    tmp_count_list.append(cnt)

    cnt=0
    for i in range(y+d1):#각 선거구 할당하기
        for j in range(x+1):
            if copy_map[i][j]==0:
                copy_map[i][j]=1
                cnt+=m[i][j]
    tmp_count_list.append(cnt)


    cnt=0
    for i in range(y+d2+1):#각 선거구 할당하기
        for j in range(x+1,N):
            if copy_map[i][j]==0:
                copy_map[i][j]=2
                cnt+=m[i][j]
    tmp_count_list.append(cnt)

    cnt=0
    for i in range(y+d1,N):#각 선거구 할당하기
        for j in range(x-d1+d2):
            if copy_map[i][j]==0:
                copy_map[i][j]=3
                cnt+=m[i][j]
    tmp_count_list.append(cnt)

    cnt=0
    for i in range(y+d2+1,N):#각 선거구 할당하기
        for j in range(x-d1+d2,N):
            if copy_map[i][j]==0:
                copy_map[i][j]=4
                cnt+=m[i][j]
    tmp_count_list.append(cnt)

    max_cnt=max(tmp_count_list)
    min_cnt=min(tmp_count_list)




    return max_cnt-min_cnt


def dfs():
    global max_cnt_num
    for d1 in range(N):
        for d2 in range(N):
            for i in range(N):
                for j in range(N):
                    if checkRange(j,i,d1,d2)==True: #기준점의 조건을 충족한다면
                        start_list.append([j,i,d1,d2])

    for i in range(len(start_list)):
        max_cnt_num=min(max_cnt_num,make_border(start_list[i][0],start_list[i][1],start_list[i][2],start_list[i][3]))


max_cnt_num=2000
five_sector=[]
start_list=[]#기준점을 담는 리스트
dfs()
print(max_cnt_num)