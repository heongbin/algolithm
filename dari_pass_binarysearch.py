def cal(mid,k,stones):
    cnt=0
    for i in range(len(stones)):
        if stones[i]-mid<0:
            cnt+=1
        else:
            cnt=0
        if cnt==k:
            return False

    return True


def solution(stones, k):
    left =0
    right = 200000000
    while left<=right:
        mid = (left + right)//2
        if cal(mid,k,stones)==False:
            right = mid - 1
        else:
            left = mid + 1

    return mid


stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k = 3

print(solution(stones,k))