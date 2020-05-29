import math
import decimal
#인형의 개수 N개 , 그 인형들중 연속되는 인형 K개를 고름
N , K = map(int, input().split())
#각 인형N개의 선호하는사람수를 나타내는 배열.
like_doll=list(map(int, input().split()))
answer=decimal.Decimal('INF')

sums=[0 for i in range(N+1)]
sqr_sum=sums[:]

for i in range(1,N+1):
    sums[i]=sums[i-1]+like_doll[i-1]
    sqr_sum[i]=sqr_sum[i-1]+like_doll[i-1]**2


for cnt in range(K,N+1):
    for a in range(N-cnt+1):
        m=decimal.Decimal(sums[a+cnt]-sums[a])/cnt #평균
        bs=decimal.Decimal((sqr_sum[a+cnt]-sqr_sum[a])/K)-(m*m) #분산
        answer=min(answer,bs)



print(answer.sqrt())