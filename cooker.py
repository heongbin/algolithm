
def pick_food(tmp):
    sums=0
    for i in range(len(tmp)-1):
        for j in range(i+1,len(tmp)):
            sums+=m[tmp[i]][tmp[j]]+m[tmp[j]][tmp[i]]

    another_list=[]
    for i in range(N):
        if i not in tmp:
            another_list.append(i)

    another_sums=0
    for i in range(len(another_list)-1):
        for j in range(i+1,len(another_list)):
            another_sums+=m[another_list[i]][another_list[j]]+m[another_list[j]][another_list[i]]

    return abs(another_sums-sums)



def dfs(start,cnt):
    global tmplist
    global max_num
    if cnt==N/2:
        max_num=min(max_num,pick_food(tmplist))
        return


    for i in range(start,N):
        tmplist.append(i)
        dfs(i+1,cnt+1)
        tmplist.pop()





T=int(input())
for test_case in range(1,T+1):
    max_num = 100000000
    N=int(input())
    tmplist = []
    m=[[0 for _ in range(N)] for _ in range(N)] #N/2로 A손님과 B손님에게 줄려고함.
    for i in range(N):
        m[i]=list(map(int,input().split()))
    dfs(0,0)
    print("#{} {}".format(test_case,max_num))