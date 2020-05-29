class Tree:
    def __init__(self,x,y,age):
        self.x=x
        self.y=y
        self.age=age
        self.live=True



def check_range(x,y):
    if x<0 or x>=N or y<0 or y>=N:
        return False
    return True


def spring(): #봄에는 나무가 자기 나이만큼 양분을 흡수. 양분만큼 먹고 나이 1+
    cnt=0
    for i in range(len(tree_list)):
        if tree_list[i].age<=m[tree_list[i].y][tree_list[i].x] :
            m[tree_list[i].y][tree_list[i].x]-=tree_list[i].age #양분을 자기나이만큼 먹고
            tree_list[i].age+=1 #1up

        else:
            tree_list[i].live=False
            cnt+=1






def summer(): #여름은 봄에 die한 나무가 양분이됨 그 나무의 /2가 양분으로 추가됨.
    global tree_list
    tmplist=[]
    for i in range(len(tree_list)):
        if tree_list[i].live==False:
            energy=tree_list[i].age//2 #그 나무의 양분
            m[tree_list[i].y][tree_list[i].x]+=energy
        else:
            tmplist.append(tree_list[i])

    tree_list=tmplist




def fall(): #가을에는 나무가 번식 자기 주위로 8칸에 나이가1인 나무가 생김. 물론 5의 배수인 나무만.
    global tree_list
    tmplist=[]


    for i in range(len(tree_list)):
        if tree_list[i].age%5==0 and tree_list[i].live==True: #5의 배수이면
            for j in range(8):
                nx = tree_list[i].x + dx[j]
                ny = tree_list[i].y + dy[j]
                if check_range(nx,ny)==True: #새 자식나무들이 범위를 x면
                    tmplist.append(Tree(nx,ny,1))



    for i in range(len(tree_list)):
        tmplist.append(tree_list[i])

    tree_list=tmplist






def winter(): #겨울에는 봇이 양분을 줌.
    for i in range(N):
        for j in range(N):
            m[i][j]+=a[i][j]






dx=[-1,-1,0,1,1,1,0,-1]
dy=[0,-1,-1,-1,0,1,1,1]



N,M,K = map(int,input().split())

#한변의길이가 N인 땅에 어린나무 M개를 심음. K year후에 땅에 남아있는 나무의 수를 구함.



m=[[5 for _ in range(N)] for _ in range(N)] #농사 start

a=[[0 for _ in range(N)] for _ in range(N)]

for i in range(N): #겨울에 로봇이주는 양분의 양
    a[i] = list(map(int,input().split()))


tree_list=[] #나무의 정보를 담는 리스트.
for i in range(M): #각각 x,y,age
    x,y,age = map(int,input().split())
    tree_list.append(Tree(x-1,y-1,age))



tree_list.sort(key=lambda x : x.age)






for i in range(K):
    spring()
    summer()
    fall()
    winter()


cnt=0


print(len(tree_list))






