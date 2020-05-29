

def range_check(x,y):
    if x<0 or y<0 or x>=N or y>=N:
        return False
    return True

def find_path(x,y,cnt,visited): #길찾는 함수.
    global max_num
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if range_check(nx, ny)==True and m[ny][nx]<m[y][x] and visited[ny][nx]==0:
            visited[ny][nx]=1
            find_path(nx, ny, cnt + 1,visited)
            visited[ny][nx]=0
        else:
            max_num = max(cnt, max_num)












def pick_one():
    global m
    for t in range(len(max_height_list)): #최고봉의 리스트
        for i in range(N):
            for j in range(N):
                if i==max_height_list[t][0] and j==max_height_list[t][1]:
                    continue

                for k in range(K+1): #깊이
                    visited=[[0 for _ in range(N)] for _ in range(N)]
                    m[i][j]-=k

                    visited[max_height_list[t][0]][max_height_list[t][1]]=1
                    find_path(max_height_list[t][1],max_height_list[t][0],1,visited)
                    m[i][j]+=k

dx=[-1,1,0,0]
dy=[0,0,-1,1]


T=int(input())

for test_case in range(1,T+1):
    max_num=0
    N,K =map(int,input().split())
    #visited=[[0 for _ in range(N)] for _ in range(N)]
    m=[[0 for _ in range(N)] for _ in range(N)]
    tmp_list = []
    for i in range(N):
        m[i]=list(map(int,input().split()))

    for i in range(N):
        for j in range(N):
            tmp_list.append(m[i][j])

    tmpsetlist=list(set(tmp_list))
    max_height=max(tmpsetlist)#최고높이


    max_height_list=[]
    for i in range(N):
        for j in range(N):
            if m[i][j]==max_height:
                max_height_list.append([i,j])


    pick_one()


    print(max_num)