s="{{20,111},{111}}"

answerlist=[]
s=s[1:-1]
tmps=s.split("},{")
tmps[0]=tmps[0][1:]
tmps[-1]=tmps[-1][:-1]
numlist=[]
tmplist=[]
for i in range(len(tmps)):
    tmplist=tmps[i].split(',')
    tmplist=list(map(int,tmplist))
    numlist.append(tmplist)

sortlist=sorted(numlist,key=lambda x: len(x))


answer=[]
start=sortlist[0][0]
answer=[start]
if len(sortlist)>=2:
    for i in range(1,len(sortlist)):
        for j in range(len(sortlist[i])):
            if sortlist[i][j] not in answer and sortlist[i][j]!=answer[-1]: #전배열에 추가된애
                answer.append(sortlist[i][j])
                break






print(answer)


