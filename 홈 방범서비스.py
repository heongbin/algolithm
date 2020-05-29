from collections import deque
def check_range(x,y):
    if x<0 or y<0 or x>N-1 or y>N-1:
        return False
    return True


def spread_blue(x,y,final_k): #맵 전체에 한칸마다 망을 설피해보며 고객을 몇명확보햇나 확인.
    q=deque([[x,y,0]])


    visited[y][x]=1
    cnt=0 #고객 카운트
    if m[y][x]==1:
        cnt=1

    while q:
        cur=q.popleft()
        #print(cur)
        x = cur[0]
        y = cur[1]
        k = cur[2]




        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if check_range(nx,ny)==False:
                continue
            if visited[ny][nx]==1:
                continue
            if k+1>=final_k:
                continue
            if m[ny][nx] == 1:  # 고객이 있다면
                cnt += 1
            visited[ny][nx]=1
            q.append([nx,ny,k+1])


    return cnt




#1,1/ 2,5 / 3,

#운영=pow(k,2) + pow(k-1,2)
dx=[-1,1,0,0]
dy=[0,0,-1,1]


T=int(input())
for test_case in range(1,T+1):
    max_h=0
    N,M =map(int,input().split())
    m=[[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        m[i]=list(map(int,input().split()))

    for i in range(N):
        for j in range(N):
            for k in range(1,40):
                visited=[[0 for _ in range(N)] for _ in range(N)]
                cur_customer=spread_blue(i, j, k)
                if (pow(k,2)+pow(k-1,2))-M*cur_customer<=0: #손해가 x면
                    max_h=max(max_h,cur_customer)



    print("#{} {}".format(test_case,max_h))








