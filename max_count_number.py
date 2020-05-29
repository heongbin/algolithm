T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    number=int(input())
    score_list=list(map(int,input().split()))
    dic_count={}
    for i in range(101):
        dic_count[i]=0
    for i in range(101):
        for j in range(len(score_list)):
            if i==score_list[j]:
                dic_count[i]+=1
    valuelist=list(dic_count.values())
    minnumber=0
    for i in range(len(valuelist)):
        if minnumber<=valuelist[i]:
            minnumber=valuelist[i]
            minindex=i

    keylist=list(dic_count.keys())
    print("#{} {}".format(test_case,minindex))