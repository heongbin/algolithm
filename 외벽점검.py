import copy
def permu(cnt,dist,tmplist,visited):
    global final_list
    if cnt==len(dist):
        copy_list=tmplist[:]
        final_list.append(copy_list)
        return

    for i in range(len(dist)):
        if visited[i]==0:
            tmplist.append(dist[i])
            visited[i]=1
            permu(cnt+1,dist, tmplist,visited)
            visited[i]=0
            tmplist.pop()


def check_path(start,weak,n,tmpdist):
    global answer
    new_weak_list=[]


    for i in range(start,len(weak)):
        new_weak_list.append(weak[i])
    for i in range(start):
        new_weak_list.append(weak[i]+n)




    current=new_weak_list[0]
    cnt=0

    flag=0
    for i in range(1,len(new_weak_list)):
        if current+tmpdist[cnt]<new_weak_list[i]:
            if cnt==len(tmpdist)-1:
                flag=1
                break

            cnt+=1
            current=new_weak_list[i]



    if flag==0:
        answer=min(answer,cnt+1)
        return answer

    return answer





answer=10
final_list=[]

def solution(n, weak, dist):
    global answer
    visited=[0 for _ in range(len(dist))]
    weak_list=[]
    dist.sort(reverse=True)
    permu(0,dist,[],visited)




    for i in range(len(weak)):
        for j in range(len(final_list)):
            answer=check_path(i,weak,n,final_list[j])

    if answer==10:
        return -1

    return answer



n=12
weak=[1, 3, 4, 9, 10]
dist=[3, 5, 7,9,11]
print(solution(n,weak,dist))

print(final_list[0])