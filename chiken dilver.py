# N*N크기의 도시

#1은 집 2는 치킨

#N , M 은 최대 고를 치킨집개수
N,M = map(int, input().split())
m=[[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    m[i]=list(map(int,input().split()))


class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

chiken_lst=[]
customer_lst=[]
pick_chiken_lst=[]
min_value=1000000



for i in range(N):
    for j in range(N):
        if m[i][j]==2:
            chiken_lst.append(Point(j,i))
        elif m[i][j]==1:
            customer_lst.append(Point(j,i))


def dfs(st,cnt):
    global pick_chiken_lst
    global chiken_answer
    global min_value
    if cnt==M:
        chiken_answer=0
        for i in range(len(customer_lst)):
            chiken_distance=1000000
            for j in range(len(pick_chiken_lst)):
                chiken_distance=min(chiken_distance,abs(pick_chiken_lst[j].x-customer_lst[i].x)+abs(pick_chiken_lst[j].y-customer_lst[i].y))
            chiken_answer+=chiken_distance
        min_value=min(min_value,chiken_answer)

    for i in range(st,len(chiken_lst)):
        pick_chiken_lst.append(chiken_lst[i])
        dfs(i+1,cnt+1)
        pick_chiken_lst.pop()

dfs(0,0)
print(min_value)


