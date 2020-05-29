from collections import deque

def bfs():
    global answer
    q=deque([N])
    while q:
        tmp=q.popleft()
        if tmp==K:
            answer=time[tmp]
            return
        for next_number in [tmp+1,tmp-1,tmp*2]:
            if next_number>=0 and next_number<=100000 and time[next_number]==0:
                time[next_number]=time[tmp]+1
                q.append(next_number)







N,K = map(int,input().split())
time=[0 for _ in range(100001)]
answer=0
bfs()
print(answer)