import copy
dx=[1,-1,0,0]
dy=[0,0,-1,1]




def dfs(each_tmplist,depth,copy_m,cnt,core):
    global answer
    global max_core
    if depth==len(each_tmplist):
        if core>=max_core:
            if core == max_core:
                if answer>cnt:
                    answer=cnt
                    return
                else:
                    return

            max_core=core
            answer=cnt
            return
        return





    if len(tmplist)-depth+core<max_core:
        return

    x=each_tmplist[depth][0]
    y=each_tmplist[depth][1]


    for i in range(4):
        nx = x
        ny = y
        copy_cnt = cnt
        copy_mm=[[0 for _ in range(n)] for _ in range(n)]
        for k in range(n):
            copy_mm[k]=copy_m[k][:]


        while True:
            nx+=dx[i]
            ny+=dy[i]
            if copy_mm[ny][nx]==1 or copy_mm[ny][nx]==2:#선은 2
                dfs(each_tmplist,depth+1,copy_m,cnt,core)
                break

            if ny == n - 1 or nx == n - 1 or nx == 0 or ny == 0:
                copy_mm[ny][nx]=2
                copy_cnt+=1
                dfs(each_tmplist,depth+1,copy_mm,copy_cnt,core+1)
                break

            copy_mm[ny][nx]=2
            copy_cnt+=1







def making_simul():
    dfs(tmplist,0,m,0,0)















T=int(input())
for test_case in range(1,T+1):
    max_core=0
    answer=1000
    tmplist=[]
    n=int(input())
    m=[[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        m[i]=list(map(int,input().split()))

    for i in range(n):
        for j in range(n):
            if m[i][j]==1:
                if i==0 or i==n-1 or j==0 or j==n-1:
                    continue
                tmplist.append([j,i])

    entire_tmplist=[]
    visited=[0 for _ in range(len(tmplist))]
    making_simul()

    print("#{} {}".format(test_case,answer))







