import copy
n=int(input())
m=[0 for _ in range(n)]
m=list(map(int,input().split()))
dp=copy.deepcopy(m)


max_num=0
for i in range(1,n):
    dp[i]=max(dp[i],dp[i-1]+dp[i])
    if max_num<dp[i]:
        max_num=dp[i]

print(max_num)