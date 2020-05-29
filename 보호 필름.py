import copy
from collections import deque

def permutation_AB(selected_row_list,pick_len,cnt): #줄에 넣을 AB조합을 만드는함수.
    global arr
    global m
    if cnt==pick_len: #a,b조합이 완성됨.
        tmp_list=[[0 for _ in range(W)] for _ in range(len(selected_row_list))]
        for row in range(len(selected_row_list)):
            tmp_list[row] = m[selected_row_list[row]][:]
            m[selected_row_list[row]] = [arr[row] for _ in range(W)]

        if check_correct(m) == True:
            return True


        for row in range(len(selected_row_list)):
            m[selected_row_list[row]]=tmp_list[row][:]
        return False



    for i in range(2):
        arr.append(ab_list[i])
        if permutation_AB(selected_row_list,pick_len,cnt+1)==True:
            return True
        arr.pop()








def check_correct(m): #검사 함수.
    entire_cnt = 0  # 라인전체의 개수를 검사하는 변수

    for i in range(W):
        flag=0
        cnt = 1  # 한 라인을 검사할때마다.
        for j in range(1, D):
            if m[j][i] == m[j-1][i]:  # 전과 같으면
                cnt += 1
            else:  # 전과 다르면
                if D-j-1<K-1:
                    return False
                cnt = 1

            if cnt >= K:  # 기준점을 만족시킨다면.
                flag=1
                entire_cnt += 1
                break

        if flag==0:
            return False



    if entire_cnt == W:  # 추가 할 필요x
        return True





def dfs(start,cnt, max_cnt):  # A와B를 석어서
    global answer
    if cnt == max_cnt: #선택할 row들을 담앗음.
        if permutation_AB(select_row,len(select_row),0) == True:  # 기준을 통과할 수 있게됨.
            return True
        return False

    for i in range(start,D):
        select_row.append(i)  # 일단 선택할 row를 담음.
        if dfs(i+1,cnt + 1,max_cnt)==True:
            return True
        select_row.pop()




T=int(input())
ab_list = [0, 1]
for test_case in range(1,T+1):
    select_row = []
    arr = []

    D,W,K = map(int,input().split()) #K는 기준점
    m=[[0 for _ in range(W)] for _ in range(D)]

    for i in range(D):
        m[i]=list(map(int,input().split()))


    if K==1:
        print("#{} {}".format(test_case,0))
        continue

    if check_correct(m)==True:
        answer=0

    else:
        for i in range(1,K+1):
            if i==K:
                answer=K
                break
            if dfs(0,0,i)==True:
                answer=i
                break


    print("#{} {}".format(test_case,answer))
