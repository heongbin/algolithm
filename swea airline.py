T=int(input())

def check_load_horizon(x,y):
    cur=m[y][x]
    cnt=1
    flag=0
    for i in range(1,N):
        if abs(cur-m[y][i])>=2:
            return False

        if m[y][i]==cur:
            cnt+=1

        elif m[y][i]-cur==1: #경사로라면
            if cnt-X<0:
                return False
            cnt=0
            cur=m[y][i]
            cnt+=1

        elif m[y][i]-cur==-1: #내리
            if cnt>=0:
                cnt=0
                cnt-=X
                cur=m[y][i]
                cnt+=1

            else:
                return False
    if cnt<0:
        return False
    return True



def check_load_vertical(x,y):
    cur = m[y][x]
    cnt = 1
    for i in range(1,N):
        if abs(cur-m[i][x])>=2:
            return False

        if m[i][x] == cur:
            cnt += 1

        elif m[i][x] - cur == 1:  # 경사로라면
            if cnt - X < 0:
                return False
            cnt=0
            cur=m[i][x]
            #cnt-=X
            cnt+=1

        elif m[i][x] - cur == -1:  # 내리
            if cnt >= 0:
                cnt=0
                cnt -=X
                cur = m[i][x]
                cnt+=1


            else:
                return False
    if cnt<0:
        return False
    return True

for test_case in range(1,T+1):
    N,X= map(int,input().split())
    m=[[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        m[i]=list(map(int,input().split()))

    answer=0
    if check_load_horizon(0,0)==True:
        answer+=1

    if check_load_vertical(0,0)==True:
        answer+=1

    for i in range(1,N):
        if check_load_horizon(0,i)==True:
            answer+=1

    for i in range(1,N):
        if check_load_vertical(i,0)==True:
            answer+=1

    print("#{} {}".format(test_case,answer))
