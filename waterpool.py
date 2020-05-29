def sum_numbers(visited,tmplist):
    sums=0
    cnt=0
    for i in range(len(visited)):
        if visited[i]!=0:
            if visited[i]==3:
                cnt+=1
            elif visited[i]==1:
                sums+=plan[i]*a
            elif visited[i]==2:
                sums+=b
    if cnt%3==0:
        three_month = cnt // 3
    else:
        three_month= cnt//3 + 1


    sums+=three_month*c
    return sums





def dfs(cnt,tmplist,visited,answer):
    if cnt==len(tmplist):
        answer=min(answer,sum_numbers(visited,tmplist))
        return answer

    #for i in range(start,len(tmplist)):
    if visited[tmplist[cnt][1]]==0:
        visited[tmplist[cnt][1]]=1
        answer=dfs(cnt+1,tmplist,visited,answer) #one day
        visited[tmplist[cnt][1]]=0
        visited[tmplist[cnt][1]]=2
        answer=dfs(cnt+1,tmplist,visited,answer) #one day #one month
        visited[tmplist[cnt][1]]=0
        visited[tmplist[cnt][1]]=3

        if tmplist[cnt][1]+1<=len(visited)-1:
            visited[tmplist[cnt][1]+1]=3
        if tmplist[cnt][1]+2<=len(visited)-1:
            visited[tmplist[cnt][1]+2]=3
        answer=dfs(cnt+1,tmplist,visited,answer)
        visited[tmplist[cnt][1]]=0

        if tmplist[cnt][1] + 1 <= len(visited) - 1:
            visited[tmplist[cnt][1]+1]=0
        if tmplist[cnt][1] + 2 <= len(visited) - 1:
            visited[tmplist[cnt][1]+2]=0

    elif visited[tmplist[cnt][1]]!=0:
        answer=dfs( cnt + 1, tmplist, visited, answer)

    return answer

T=int(input())
for test_case in range(1,T+1):
    a,b,c,d=map(int,input().split())
    plan=[0 for _ in range(12)]
    visited=[0 for _ in range(12)]
    #visited 1=oneday,2=one month ,3=3month , 4=year
    plan=list(map(int,input().split()))

    tmplist=[]
    for i in range(len(plan)):
        if plan[i]!=0:
            tmplist.append([plan[i],i])

    answer=1100000
    answer=dfs(0,tmplist,visited,answer)
    answer=min(answer,d)
    print("#{} {}".format(test_case,answer))




