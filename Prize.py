


def dfs(arrlst, cnt):
    global answer
    global visit

    arr = "".join(arrlst)

    if cnt==change:
        tmp = int(arr)
        if tmp > answer:
            answer = tmp
            return
        return

    for i in range(len(arrlst)):
        for j in range(i + 1, len(arrlst)):
            arrlst[i], arrlst[j] = arrlst[j], arrlst[i]
            arr = "".join(arrlst)
            if visited[cnt+1][int(arr)] == 0:
                visited[cnt+1][int(arr)] = 1
                #print("check{}{}".format(i,j))
                dfs(arrlst, cnt + 1)
                #print("check1")
            arrlst[i], arrlst[j] = arrlst[j], arrlst[i]

visited = [[0 for _ in range(1000000-1)] for _ in range(11)]
T = int(input())
for test_case in range(1, T + 1):
    number, change = map(int, input().split())
    numstr = list(str(number))

    # 문자열을 리스트배열로 저장 str형태임
    answer = 0
    visit=visited[:]
    dfs(numstr, 0)
    print("#{} {}".format(test_case,answer ))
