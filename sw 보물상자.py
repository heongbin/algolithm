from collections import deque
def spread_number(m):
    m=list(m)
    for i in range(0,len(m),each_split):
        number_list.append("".join(m[i:i+each_split]))
    m=deque(m)




T=int(input())
for test_case in range(1,T+1):
    N,K = map(int,input().split())
    m=["" for _ in range(N)]
    m=deque(list(str(input())))
    each_split=N//4
    number_list=[]
    spread_number(m)

    for i in range(1,N//4):
        tmp=m.popleft()
        m.append(tmp)
        spread_number(m)


    final_list=list(set(number_list))

    tmp_list=[]
    for i in range(len(final_list)):
        sums=0
        cnt=0
        for k in range(len(final_list[i])-1,-1,-1):
            if final_list[i][k].isdigit()==True:
                tmp=int(final_list[i][k])
            else:
                if final_list[i][k]=="A":
                    tmp=10
                elif final_list[i][k]=="B":
                    tmp=11
                elif final_list[i][k]=="C":
                    tmp=12
                elif final_list[i][k]=="D":
                    tmp=13
                elif final_list[i][k]=="E":
                    tmp=14
                else:
                    tmp=15

            tmp=tmp*pow(16,cnt)
            cnt+=1
            sums+=tmp
        tmp_list.append(sums)

    tmp_list.sort(reverse=True)
    print("#{} {}".format(test_case,tmp_list[K-1]))





