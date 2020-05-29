N=int(input())
numbers=[0 for _ in range(N)]
numbers= list(map(int,input().split()))
corp=[0 for _ in range(4)]
corp=list(map(int,input().split()))


sums_list=[]
def dfs(idx,sums,corp):
    global sums_list
    if idx==N:
        sums_list.append(sums)
        return

    if corp[0]!=0:
        tmp_corp=corp[:]
        tmp_corp[0]-=1
        dfs(idx + 1,sums+numbers[idx],tmp_corp)
    if corp[1]!=0:
        tmp_corp=corp[:]
        tmp_corp[1]-=1
        dfs(idx + 1,sums-numbers[idx],tmp_corp)
    if corp[2]!=0:
        tmp_corp=corp[:]
        tmp_corp[2]-=1
        dfs(idx + 1,sums*numbers[idx],tmp_corp)
    if corp[3]!=0:
        tmp_corp=corp[:]
        tmp_corp[3]-=1
        if sums<0:
            dfs(idx + 1,(sums*-1//numbers[idx])*-1,tmp_corp)
        else:
            dfs(idx+1,sums//numbers[idx],tmp_corp)




dfs(1,numbers[0],corp)



print(max(sums_list))
print(min(sums_list))
