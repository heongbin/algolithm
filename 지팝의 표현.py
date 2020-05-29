n,m = map(int,input().split())
s=[[0 for _ in range(3)] for _ in range(m)]
for i in range(m):
    s[i]=list(map(int,input().split()))


dic={x : x for x in range(n+1)}
def find(u):
    if dic[u]==u:
        return u
    dic[u]=find(dic[u])
    return dic[u]

def union(u,v):
    global dic
    u=find(u)
    v=find(v)

    dic[u]=v


for i in range(len(s)):
    if s[i][0]==0:
        union(s[i][1],s[i][2])
    elif s[i][0]==1:
        if find(s[i][1])==find(s[i][2]):
            print("yes")
        else:
            print("no")



