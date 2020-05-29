
class Data:
    def __init__(self,A,B,W,D,L):
        self.A = A
        self.B = B
        self.W = W
        self.D = D
        self.L = L






def dfs(cnt, percent):
    global score
    global Percent

    if(cnt==6):
        Total_score=[]
        for i in range(4):
            tmplst=[]
            tmplst.append(score[i])
            tmplst.append(i)
            Total_score.append(tmplst)

        Total_score.sort(key= lambda x: x[0])

        A,B,C,D = Total_score[0][0],Total_score[1][0],Total_score[2][0],Total_score[3][0]
        a,b,c,d = Total_score[0][1],Total_score[1][1],Total_score[2][1],Total_score[3][1]

        if B!=C: #다다른
            Percent[c]+=percent
            Percent[d]+=percent

        elif A==B and C==D: #전원 같은
            for i in range(4):
                Percent[i]+=percent/2

        elif A==B: #1등만 다르
            Percent[a]+=percent/3
            Percent[b] += percent / 3
            Percent[c] += percent / 3

        elif C==D:
            Percent[d]+=percent*2/3
            Percent[c]+=percent*2/3
            Percent[b]+=percent*2/3

        else: #b와 c가 같은경구
            Percent[c]+=percent/2
            Percent[b]+=percent/2
            Percent[d]+=percent

        return

    A=array[cnt].A
    B=array[cnt].B

    score[A]+=3
    dfs(cnt+1, percent*array[cnt].W)
    score[A]-=3

    score[A]+=1
    score[B]+=1
    dfs(cnt+1, percent*array[cnt].D)
    score[A]-=1
    score[B]-=1

    score[B]+=3
    dfs(cnt+1, percent*array[cnt].L)
    score[B]-=3


a,b,c,d = map(str,input().split())

dic={a:0,b:1,c:2,d:3}


m=[["" for _ in range(5)] for _ in range(6)]


for i in range(6):
    m[i]=list(map(str,input().split()))
    m[i][2],m[i][3],m[i][4] = map(float, m[i][2:])


array=[]
score=[0 for _ in range(4)]
Percent=[0 for _ in range(4)]

for i in range(6):
   array.append(Data(dic[m[i][0]],dic[m[i][1]],m[i][2],m[i][3],m[i][4]))


dfs(0,1.0)
for i in range(4):
    print(Percent[i])














