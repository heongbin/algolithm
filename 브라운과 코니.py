#브라운이 쫓는애, 코니가 쫒기는 애.

def solve1(conyPosition,brownPositon): #브라운이 시간 t일때, 코니와 브라운의 위치가 같다면 잡는걸로 간주하는 함수.
    visited=[False for _ in range(200001)]
    visited[brownPositon]=True
    q=[[brownPositon,0]]

    while q:
        cur=q.pop(0)
        currentPosition = cur[0]
        currentTime = cur[1]

        if currentPosition == conyPosition + currentTime*(currentTime+1)//2:
            return currentTime

        for next_Position in [currentPosition+1,currentPosition-1,currentPosition*2]:
            if visited[next_Position]==False:
                visited[next_Position]=True
                q.append([next_Position,currentTime+1])



def solve2(conyPosition,brownPosition): #브라운이 코니가 방문한곳을 방문하면 잡앗다고하는 함수.
    time=0
    visited=[False for _ in range(200001)]
    visited[brownPosition]=True
    q=[brownPosition]

    while True:
        conyPosition+=time

        if conyPosition>200000:
            return -1

        if visited[conyPosition]==True:
            return time

        size=len(q)

        for i in range(size):
            a=q.pop(0)
            for next_brown in [a+1,a-1,a*2]:
                if visited[next_brown]==False:
                    visited[next_brown]=True
                    q.append(next_brown)

        time+=1

def solve_final(conyPosition,brownPosition):
    time = 0
    visited = [[False for _ in range(2)] for _ in range(200001)]
    visited[brownPosition][time] = True
    q = [[brownPosition,0]]

    while True:
        conyPosition += time

        if conyPosition > 200000:
            return -1

        if visited[conyPosition][time%2] == True: #도착한 위치가 같더라도 시간차이가 짝수나 홀수차이가 같아야 브라운이 코니를 잡을수있음 만약 같은위치인데 브라운은 타임이 홀수고 코니는 짝수면
            return time

        size = len(q)

        for i in range(size):
            a = q.pop(0)
            currentposition=a[0]
            next_time=(a[1]+1)%2

            for next_brown in [currentposition + 1, currentposition - 1, currentposition * 2]:
                if visited[next_brown][next_time] == False:
                    visited[next_brown][next_time] = True
                    q.append([next_brown,next_time])

        time += 1







print(solve_final(6,3))


