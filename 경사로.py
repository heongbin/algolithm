# N 지도의크기, L 경사로의 길이
N,L=map(int,input().split())

m=[[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    m[i]=list(map(int,input().split()))


answer=0

for i in range(N):
    cnt=1
    for j in range(1,N):
        flag=0
        D=m[i][j]-m[i][j-1]
        if D==0: #전칸과 높이가 같다.
            cnt+=1


        elif D==1 and cnt>=L:
            cnt=1


        elif D==-1 and cnt>=0:
            cnt=-L+1


        else:
            flag=1
            break

    if cnt>=0 and flag!=1:
        answer+=1

for i in range(N):
    cnt = 1
    flag=0
    for j in range(1, N):
        D = m[j][i] - m[j-1][i]
        if D == 0:  # 전칸과 높이가 같다.
            cnt += 1

        elif D == 1 and cnt >= L:
            cnt = 1


        elif D == -1 and cnt >= 0:
            cnt = -L + 1

        else:
            flag=1
            break

    if cnt>=0 and flag!=1:
        answer+=1






print(answer)
