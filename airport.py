

G = int(input())
P = int(input())

Plane_loc = [0 for _ in range(P)] #인덱스 0부터 차례대로 도착.
for i in range(P):
    Plane_loc[i] = int(input()) #각 비행기가 갈려는 게이트 번호

dic={0:0}
for i in range(1,G+1):
    dic[i] = i

cnt=0
answer=[]
flag = 0
def find(u):
    global dic
    ##global flag
    ##global answer
    ##global cnt
    #for i in range(plane_loc[idx],0,-1):
        #if dic[i] == 0: #해당 게이트가 비엇다면
            #dic[i] = 1
            #cnt+=1
            #return True

    #return False #갈수있는 게이트가 다 게이트가 찻다면.

    ##if wannagate == 1 and wannagate in answer:
        ##return -1

    ##if wannagate not in answer:
        ##answer.append(wannagate)
        ##return wannagate



    ##dic[wannagate] = find_gate(dic[wannagate])
    ##return dic[wannagate]
    if dic[u]==u:
        return u


    dic[u]=find(dic[u])
    return dic[u]




def Union(u,v):
    global dic
    u = find(u)
    v = find(v)

    dic[u]=v













answer=0

for i in range(P):
    if find(Plane_loc[i]) == 0:
        break
    else: #만약 비엇다면 비행기를 넣어주고 루트를 다음전 게이트로 정한다
        answer+=1
        Union(find(Plane_loc[i]),find(Plane_loc[i])-1)

print(answer)


