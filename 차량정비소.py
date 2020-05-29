class Customer: #각 고객의 번호와 도착시간을 받음.
    def __init__(self,idx,arrive_time):
        self.idx=idx
        self.arrive_time= arrive_time
        self.a=0
        self.b=0



T=int(input())
for test_case in range(1,T+1):
    N,M,K,A,B = map(int,input().split())
    #N접수 개수 M수리 K 고객의 수,A,B 고객이 이용한
    a=[0 for _ in range(N)] #각 걸리는 수행시간
    b=[0 for _ in range(M)]
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    k=[0 for _ in range(K)]
    k=list(map(int,input().split()))

    customer_list=[]

    for i in range(K):
        customer_list.append(Customer(i+1,k[i]))



    wait_list_a=[]
    visiteda=[[0 for _ in range(2)] for _ in range(N)] #각 SECTION마다 고객을 갖고있는지 표시.0은 빈section 다른정수면 해당 고객을 갖고잇는중 그고객이 진행상황.
    wait_list_b=[]
    visitedb=[[0 for _ in range(2)] for _ in range(M)]

    waitlist=[]

    t=0
    while True: #시간은 다넣고나서 증가시켜준다.
       check=0
       for i in range(K):
           if customer_list[i].b==0:
               check=1
               break
       if check==0:
           break


       #한 시간
       for i in range(K):
           if customer_list[i].idx not in wait_list_a:
               if customer_list[i].arrive_time<=t and customer_list[i].a==0 :
                   wait_list_a.append(customer_list[i].idx)


       wait_list_a.sort(reverse=True)

       tmplist=[]
       for i in range(N): #a구역
           if visiteda[i][0]!=0 and visiteda[i][1]==a[i]: #완료된게 있다면
               tmp=visiteda[i][0]
               visiteda[i][0]=0
               visiteda[i][1]=0
               tmplist.append(customer_list[tmp-1])

       for i in range(M):
           if visitedb[i][0]!=0 and visitedb[i][1]==b[i]:
               tmp=visitedb[i][0]
               visitedb[i][0]=0
               visitedb[i][1]=0





       tmplist.sort(key=lambda x:x.a)

       for i in range(len(tmplist)):
           wait_list_b.append(tmplist[i])





       while wait_list_a: #고객들 뽑기 해당고객은 정보에 자기가 이용한 곳 저장.
           flag=0
           for i in range(N):
               if visiteda[i][0]==0 and wait_list_a:
                   cur = wait_list_a.pop()
                   visiteda[i][0]=cur
                   customer_list[cur-1].a=i+1 #현재고객이 용하는 section 번호.
                   flag=1

           if flag==0:
               break







       while wait_list_b:
           flag=0
           for i in range(M):
               if visitedb[i][0]==0 and wait_list_b:
                   cur = wait_list_b.pop(0)
                   visitedb[i][0]=cur.idx
                   customer_list[cur.idx-1].b=i+1
                   flag=1
           if flag==0:
                break





       for i in range(len(visiteda)):
           if visiteda[i][0]!=0:
               visiteda[i][1]+=1

       for i in range(len(visitedb)):
           if visitedb[i][0]!=0:
               visitedb[i][1]+=1


       t+=1

    answer=0
    for i in range(K):
        if customer_list[i].a==A and customer_list[i].b==B:
            answer+=customer_list[i].idx

    if answer==0:
        answer=-1
    print("#{} {}".format(test_case,answer))




















                       




























