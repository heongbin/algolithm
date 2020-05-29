

def check_range(x,y):
    if x<0 or y<0 or x>=M or y>=N:
        return False
    return True

dx=[0,0,-1,1]
dy=[-1,1,0,0]



T=int(input())
for test_case in range(1,T+1):
    cnt=0
    N,M,R,C,L = map(int,input().split())
    visited = [[0 for _ in range(M)] for _ in range(N)]
    m=[[0 for _ in range(M)] for _ in range(N)]
    for i in range(len(m)):
        m[i]=list(map(int,input().split()))


    q=[[C,R,1]]
    while q:
        curr=q.pop(0)
        x=curr[0]
        y=curr[1]
        time=curr[2]
        if time==L:
            if time==1:
                cnt=1
            break
        #1234
        #상하좌우
        if m[curr[1]][curr[0]]==1:
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                if check_range(nx,ny)==False:
                    continue
                if visited[ny][nx]==1:
                    continue

                if i==0:
                    if m[ny][nx]==1 or m[ny][nx]==2 or m[ny][nx]==5 or m[ny][nx]==6:
                        visited[ny][nx]=1
                        q.append([nx,ny,time+1])
                        cnt+=1
                elif i==1:
                    if m[ny][nx]==1 or m[ny][nx]==2 or m[ny][nx]==4 or m[ny][nx]==7:
                        visited[ny][nx] = 1
                        q.append([nx, ny, time + 1])
                        cnt += 1

                elif i==2:
                    if m[ny][nx]==1 or m[ny][nx]==3 or m[ny][nx]==4 or m[ny][nx]==5:
                        visited[ny][nx] = 1
                        q.append([nx, ny, time + 1])
                        cnt += 1

                elif i==3:
                    if m[ny][nx]==1 or m[ny][nx]==3 or m[ny][nx]==6 or m[ny][nx]==7:
                        visited[ny][nx] = 1
                        q.append([nx, ny, time + 1])
                        cnt += 1






        elif m[curr[1]][curr[0]]==2:
            for i in range(2):
                nx=x+dx[i]
                ny=y+dy[i]
                if check_range(nx,ny)==False:
                    continue

                if visited[ny][nx] == 1:
                    continue

                if i == 0:
                    if m[ny][nx] == 1 or m[ny][nx] == 2 or m[ny][nx]==5 or m[ny][nx] == 6:
                        visited[ny][nx] = 1
                        q.append([nx, ny, time + 1])
                        cnt += 1
                elif i == 1:
                    if m[ny][nx]==1 or m[ny][nx] == 2 or m[ny][nx] == 4 or m[ny][nx] == 7:
                        visited[ny][nx] = 1
                        q.append([nx, ny, time + 1])
                        cnt += 1

        elif m[curr[1]][curr[0]] == 3:
            for i in range(2,4): #좌,우
                nx=x+dx[i]
                ny=y+dy[i]
                if check_range(nx,ny)==False:
                    continue

                if visited[ny][nx] == 1:
                    continue

                if i == 2:
                    if m[ny][nx] == 1 or m[ny][nx] == 3 or m[ny][nx] == 4 or m[ny][nx] == 5:
                        visited[ny][nx] = 1
                        q.append([nx, ny, time + 1])
                        cnt += 1
                elif i == 3:
                    if m[ny][nx] == 1 or m[ny][nx] == 3 or m[ny][nx] == 6 or m[ny][nx] == 7:
                        visited[ny][nx] = 1
                        q.append([nx, ny, time + 1])
                        cnt += 1

        elif m[curr[1]][curr[0]] == 4:
            for i in [0,3]:
                nx=x+dx[i]
                ny=y+dy[i]
                if check_range(nx,ny)==False:
                    continue

                if visited[ny][nx] == 1:
                    continue

                if i == 0: #위
                    if m[ny][nx] == 1 or m[ny][nx] == 2 or m[ny][nx] == 5 or m[ny][nx] == 6:
                        visited[ny][nx] = 1
                        q.append([nx, ny, time + 1])
                        cnt += 1
                elif i == 3: #우
                    if m[ny][nx] == 1 or m[ny][nx] == 3 or m[ny][nx] == 6 or m[ny][nx] == 7:
                        visited[ny][nx] = 1
                        q.append([nx, ny, time + 1])
                        cnt += 1

        elif m[curr[1]][curr[0]] == 5:
            for i in [1,3]:
                nx=x+dx[i]
                ny=y+dy[i]
                if check_range(nx,ny)==False:
                    continue

                if visited[ny][nx] == 1:
                    continue

                if i == 1:
                    if m[ny][nx] == 1 or m[ny][nx] == 2 or m[ny][nx] == 4 or m[ny][nx] == 7:
                        visited[ny][nx] = 1
                        q.append([nx, ny, time + 1])
                        cnt += 1
                elif i == 3:
                    if m[ny][nx] == 1 or m[ny][nx] == 3 or m[ny][nx] == 6 or m[ny][nx] == 7:
                        visited[ny][nx] = 1
                        q.append([nx, ny, time + 1])
                        cnt += 1

        elif m[curr[1]][curr[0]] == 6:
            for i in [1,2]:
                nx=x+dx[i]
                ny=y+dy[i]
                if check_range(nx,ny)==False:
                    continue
                if visited[ny][nx] == 1:
                    continue

                if i == 1:
                    if m[ny][nx] == 1 or m[ny][nx] == 2 or m[ny][nx] == 4 or m[ny][nx] == 7:
                        visited[ny][nx] = 1
                        q.append([nx, ny, time + 1])
                        cnt += 1
                elif i == 2:
                    if m[ny][nx] == 1 or m[ny][nx] == 3 or m[ny][nx] == 4 or m[ny][nx] == 5:
                        visited[ny][nx] = 1
                        q.append([nx, ny, time + 1])
                        cnt += 1

        elif m[curr[1]][curr[0]] == 7:
            for i in [0,2]:
                nx=x+dx[i]
                ny=y+dy[i]
                if check_range(nx,ny)==False:
                    continue
                if visited[ny][nx] == 1:
                    continue

                if i == 0:
                    if m[ny][nx] == 1 or m[ny][nx] == 2 or m[ny][nx] == 5 or m[ny][nx] == 6:
                        visited[ny][nx] = 1
                        q.append([nx, ny, time + 1])
                        cnt += 1

                elif i == 2:
                    if m[ny][nx] == 1 or m[ny][nx] == 3 or m[ny][nx] == 4 or m[ny][nx] == 5:
                        visited[ny][nx] = 1
                        q.append([nx, ny, time + 1])
                        cnt += 1


    print("#{} {}".format(test_case,cnt))







