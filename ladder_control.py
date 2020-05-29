#N 세로선의 개수 M 현재 세로선들 사이에 연결되 있는 가로선의 개수  H 세로선마다 놓을수있는 가로선의 개수
N,M,H = map(int,input().split())

m=[[0 for _ in range(2)] for _ in range(M)]
#현재 세로선들을 연결하는 가로선들의 정보들



for i in range(M):
    m[i]= list(map(int,input().split()))
    #m[0]은 ,m[1]은 m[1]세로선과 m[1]+1 세로선을 이어주는 가로선의 위치가 m[0]인것.
    #세로선은 왼쪽부터 1,+1,+1
    #가로선은 위쪽부터 아래로 1,+1,+1


#사다리로 i가 i에 도착하는 최소 추가 가로선의 개수

#일단 m을 배열화한다
ladder_map=[[0 for _ in range(N)] for _ in range(H)]
#레더가 1이면 가로선으로 연결되있음.

for k in range(M):
    flag=0
    for i in range(H):
        for j in range(N-1):
            if m[k][1]-1==j:
                if m[k][0]-1==i:
                    ladder_map[i][j]=1
                    flag=1
                    break
        if flag==1:
            break


#여기까지 기본주어진 가로선이 연결된 상태를 맵들에 표시.



def findPath(row,col): #사다리 타기.
    for i in range(H):
        if ladder_map[i][col]==0:
            if col!=0 and ladder_map[i][col-1]==1:
                col-=1
        else:
            if col!=N-1:
                col+=1

    return col
    #if row>H-1:
        #return col
    #if ladder_map[row][col]==0: #해당칸은 가로선이x
        #if col!=0 and ladder_map[row][col-1]==1: #옆에칸이 가로선이 있으면 왼쪽으로
         #   return findPath(row+1,col-1)
        #else:
           # return findPath(row+1,col)

    #else:
     #   if col!=N-1:
      #      return findPath(row+1,col+1)







def checkRight(): #정답처럼 사다리가 작동하는지 확인하는 함수.
    for i in range(N):
        if findPath(0,i)!=i: #다르다면
            return False

    return True



#가로선을 넣는것에 조건이있음. 세로방향으로는 바로 윗칸이나 아랫칸이 가로선이 X여야함.
#가로방향으로는 바로 오른쪽이나 왼쪽에 가로선이 있으면X

def dfs(start,cnt,limit): #사다리를 1개,2개,3개까지 넣는 방법을 dfs로.
    if cnt==limit:
        if checkRight()==True:
            return True
        return False

    for i in range(start,H):
        for j in range(N-1):
            if ladder_map[i][j]==0:#연결된 가로선이x
                if j>=1:
                    if ladder_map[i][j-1]==0 and ladder_map[i][j+1]==0:
                        ladder_map[i][j]=1
                        if dfs(i,cnt+1,limit)==True:
                            return True
                        ladder_map[i][j]=0
                else:
                    if ladder_map[i][j+1]==0:
                        ladder_map[i][j]=1
                        if dfs(i,cnt+1,limit)==True:
                            return True
                        ladder_map[i][j]=0

    return False






#여긴 메인 영역.
answer=0
main_cnt=1


if checkRight()==False: #가로선 추가해야함.
    while True:
        if main_cnt==4:
            answer=-1
            break
        if dfs(0,0,main_cnt)==True:
            answer=main_cnt
            break
        else:
            main_cnt+=1

else: #추가할필요x
    answer=0


print(answer)