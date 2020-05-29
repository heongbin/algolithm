import collections
#배열A는 3*3
#행의 개수>=열의 개수 R연산 정렬
#행의 개수< 열의 개수 C연산 정렬

#각 숫자의 빈도수가 큰순서대로 오름차순

#그다음 숫자가 커지는 순으로 오름차순

#1 2 1 A[1][2]=1이되기위한
#1 2 1 > 2 1 1 2 0 0
#2 1 3 > 1 1 2 1 3 1
#3 3 3 > 3 3 0 0 0 0

#1<R
#1<C
R=3
C=3


m=[[0 for _ in range(100)] for _ in range(100)]
r,c,k = map(int,input().split())
for i in range(3):
    m[i][0],m[i][1],m[i][2]=map(int,input().split())

time=0
while True:
    if m[r-1][c-1]==k:
        break

    if time>100:
        time=-1
        break



    if R>=C:
        for i in range(R): #한 행에대하여
            tmplst = [0 for _ in range(101)]
            sortlist=[]

            for j in range(C):
                tmplst[m[i][j]]+=1

            for j in range(100):
                m[i][j]=0

            for j in range(1,len(tmplst)):
                if tmplst[j]!=0:
                    sortlist.append([j,tmplst[j]])

            newsortlist=sorted(sortlist,key=lambda x:(x[1], x[0]))

            j=0
            for a in range(len(newsortlist)):
                m[i][j]=newsortlist[a][0]
                m[i][j+1]=newsortlist[a][1]
                j+=2


    else:
        for i in range(C): #열에 대하여
            tmplst = [0 for _ in range(101)]
            sortlist = []
            for j in range(R):
                tmplst[m[j][i]]+=1

            for j in range(100):
                m[j][i]=0

            for j in range(1,len(tmplst)):
                if tmplst[j]!=0:
                    sortlist.append([j,tmplst[j]])

            newsortlist=sorted(sortlist,key=lambda x:(x[1], x[0]))


            j=0
            for a in range(len(newsortlist)):
                m[j][i]=newsortlist[a][0]
                m[j+1][i]=newsortlist[a][1]
                j+=2


    ni=0
    nj=0
    for i in range(100):
        for j in range(100):
            if m[i][j]!=0:
                ni=max(ni,i)
                nj=max(nj,j)
    R=ni+1
    C=nj+1

    time += 1


print(time)






