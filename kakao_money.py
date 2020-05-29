T=int(input())
m=[[0 for _ in range(2)] for _ in range(T)]
for i in range(T):
    m[i]=list(map(int,input().split()))

def gcd(a,b):
    while b!=0:
        temp=a%b
        a=b
        b=temp
    return a
flag=0
min_b=pow(10,18)
last_b=0 #잔액
M=0  #충전할금액
for i in range(T):
    if m[i][0]+last_b<0: #잔액보다 송금해야 할 금액이 크면
        if m[i][1]!=0 and m[i][1]<min_b:
            min_b=m[i][1]
        tmpM=m[i][1]-m[i][0]-last_b #충전할금액 후보
        if M==0: #충전한적이X면
            M=tmpM
        else: #충전한적 있음
            M=gcd(M,tmpM)
            if M<=min_b and min_b!=pow(10,18): #
                flag=1
                break
    else: #잔액이 송금금액보다 클때
        if m[i][0]+last_b!=m[i][1]:
            flag=1
            break
    last_b=m[i][1]

if flag==0 and M!=0:
    print(M)
elif flag==0 and M==0: #충전X
    print(1)
elif flag==1:
    print(-1)









