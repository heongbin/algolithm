from collections import deque
import copy
N,M,T = map(int,input().split())
#반지름 n,n-1,n-2,n-3,...
#M 원판하나에 있는 숫자개수.
#T는 회전횟수.
m=[[0 for _ in range(M)] for _ in range(N)]
for i in range(N):#각원판에 적힌 수 i행 원판i
    m[i]=deque(list(map(int,input().split())))



t=[[0 for _ in range(3)] for _ in range(T)]

for i in range(T):
    t[i]=list(map(int,input().split()))
#t=[[x,d,k],[],[],[]]
#x의 배순인 원판들 회전  d방향으로 k번 회전
#d는 0시계 1반시계





for i in range(len(t)):
    for j in range(1,N//t[i][0]+1): #각원판마다 실행되는 구간
        if t[i][1]==0: #시계방향 pop,appendleft
            for k in range(t[i][2]):
                tmp=m[t[i][0]*j-1].pop()         #안에있는 최소배수의 원판부터 ,해당원판
                m[t[i][0]*j-1].appendleft(tmp)


        else:           #qks popleft,append
            for k in range(t[i][2]):
                tmp=m[t[i][0]*j-1].popleft()         #안에있는 최소배수의 원판부터 ,해당원판
                m[t[i][0]*j-1].append(tmp)


    copym=copy.deepcopy(m)
    entire_flag=0
    for j in range(len(m)): #각원판마다 근처 숫자 확인
        for k in range(len(m[j])):#한 원판의 숫자들을 확인
            flag=0
            if m[j][k]==m[j][(k+1)%M] and m[j][k]!=0: #같은원판의 옆숫자확인
                copym[j][(k+1)%M]=0
                if flag==0:
                    flag=1
            if m[j][k]==m[j][(k+(M-1))%M] and m[j][k]!=0: #같은 원판의 오른숫자확인
                copym[j][(k+(M-1))%M]=0
                if flag==0:
                    flag=1
            if j!=0:
                if m[j][k]==m[j-1][k] and m[j][k]!=0: #안쪽의 원판의 같은 위치의 숫자와 비교
                    copym[j-1][k]=0
                    if flag==0:
                        flag=1

            if j!=N-1:
                if m[j][k] == m[j+1][k] and m[j][k]!=0:
                    copym[j+1][k]=0
                    if flag==0:
                        flag=1



            if flag==1:
                copym[j][k]=0
                if entire_flag==0:
                    entire_flag=1

    if entire_flag==0: #인접한숫자중에 같은게 x
        sums=0
        cnt=0
        for j in range(len(m)):
            for k in range(len(m[0])):
                if m[j][k]!=0:
                    cnt+=1
        for j in range(len(m)):
            sums+=sum(m[j])
        if cnt==0:
            sums=0
        else:
            sums=sums/cnt

        for j in range(len(m)):
            for k in range(len(m[0])):
                if m[j][k] != 0 and m[j][k]>sums:
                    m[j][k]-=1
                elif m[j][k]!=0 and m[j][k]<sums:
                    m[j][k]+=1
    else: #같은게 있다면
        m=copy.deepcopy(copym)


sums=0
for j in range(len(m)):
    sums+=sum(m[j])


print(sums)





