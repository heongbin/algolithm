
def find(dic,u):
    if dic[u]==u:
        return u

    dic[u]=find(dic,dic[u])
    return dic[u]

def union(dic,u,v):
    u=find(dic,u)
    v=find(dic,v)

    dic[u]=v

def solution(k, room_number):
    dic={}
    answer=[]

    for i in range(k):
        dic[i+1]=i+1

    for room in room_number:
        answer.append(find(dic,room))
        dic[find(dic,room)] = find(dic,find(dic,room)+1)
    return answer

room_number=[1,3,4,1,3,1]
k=10
print(solution(k,room_number))








