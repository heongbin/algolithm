

def spread(v,idx,flag):
    if flag==1: #오른쪽으로 퍼짐
        curr = idx + 1
        if curr<=len(v)-1:
            while v[curr]!=0:
                v[curr]=v[idx]
                if curr==len(v)-1:
                    break
                curr+=1





    elif flag==0: #왼쪽으로
        curr=idx-1
        if idx-1>=0:
            while v[curr]!=0:
                v[curr]=v[idx]
                if curr == 0:
                    break
                curr-=1

    return v





def caluculate(tmplist):
    global number_list
    print(tmplist)
    number_list=list(map(int,number_list))
    visited = [0 for _ in range(len(number_list))]
    for i in range(len(tmplist)):
        for j in range(len(yeon)):
            if yeon[j]==tmplist[i]:
                if yeon[j]=="+":
                    if visited[j]==0 and visited[j+1]==0: #선택한 연산자의 양옆 숫자가 모두 첨이라면.
                        visited[j]=number_list[j]+number_list[j+1]
                        visited[j+1]=visited[j]


                    elif visited[j]==0 and visited[j+1]==1:
                        visited[j]=visited[j+1]+number_list[j]
                        visited[j+1]=visited[j]
                        visited=spread(visited,j+1,1)


                    elif visited[j]==1 and visited[j+1]==0:
                        visited[j+1]=visited[j]+number_list[j+1]
                        visited[j]=visited[j+1]
                        visited=spread(visited,j,0)

                    elif visited[j]==1 and visited[j+1]==1:
                        visited[j]=visited[j]+visited[j+1]
                        visited[j+1]=visited[j]
                        visited=spread(visited,j+1,1)
                        visited=spread(visited,j,0)

                elif yeon[j]=="-":
                    if visited[j]==0 and visited[j+1]==0: #선택한 연산자의 양옆 숫자가 모두 첨이라면.
                        visited[j]=number_list[j]-number_list[j+1]
                        visited[j+1]=visited[j]


                    elif visited[j] == 0 and visited[j + 1] != 0:
                        visited[j] = visited[j + 1] - number_list[j]
                        visited[j + 1] = visited[j]
                        visited=spread(visited, j + 1, 1)

                    elif visited[j] !=0 and visited[j + 1] == 0:
                        visited[j + 1] = visited[j] - number_list[j + 1]
                        visited[j] = visited[j + 1]
                        visited=spread(visited, j, 0)

                    elif visited[j] !=0 and visited[j + 1] !=0:
                        visited[j] = visited[j] - visited[j + 1]
                        visited[j + 1] = visited[j]
                        visited=spread(visited, j + 1, 1)
                        visited=spread(visited, j, 0)





                else:
                    if visited[j]==0 and visited[j+1]==0: #선택한 연산자의 양옆 숫자가 모두 첨이라면.
                        visited[j]=number_list[j]*number_list[j+1]
                        visited[j+1]=visited[j]

                    elif visited[j] == 0 and visited[j + 1] != 0:
                        visited[j] = visited[j + 1] * number_list[j]
                        visited[j + 1] = visited[j]
                        visited=spread(visited, j + 1, 1)

                    elif visited[j] != 0 and visited[j + 1] == 0:
                        visited[j + 1] = visited[j] * number_list[j + 1]
                        visited[j] = visited[j + 1]
                        visited=spread(visited, j, 0)


                    elif visited[j] != 0 and visited[j + 1] != 0:
                        visited[j] = visited[j] * visited[j + 1]
                        visited[j + 1] = visited[j]
                        visited=spread(visited, j + 1, 1)
                        visited=spread(visited, j, 0)

    print(visited)
    return visited[0]




def permu(n,cnt,tmplist):
    global answer
    if cnt==n:
        answer=max(answer,caluculate(tmplist))
        return

    for i in range(len(setyeon)):
        if tmp_visited[i]==0:
            tmp_visited[i]=1
            tmplist.append(setyeon[i])
            permu(n,cnt+1,tmplist)
            tmp_visited[i]=0
            tmplist.pop()



words="3+4-5*2+3"
number_list=[]
yeon=[]

start=0
for i in range(len(words)):
    if words[i].isdigit()==False:
        number_list.append(words[start:i])
        yeon.append(words[i])
        start=i+1


number_list.append(words[start:])

visited=[0 for _ in range(len(number_list))]



setyeon=list(set(yeon))

tmp_visited=[0 for _ in range(len(setyeon))]
answer=0

permu(len(setyeon),0,[])
print(answer)

