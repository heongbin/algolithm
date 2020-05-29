import copy
class Horse:
    def __init__(self,road,location):
        self.road=road
        self.loc=location
        self.finished=False

def CheckInHorse(road,loc):
    for i in range(4):
        if rane[horse[i].road][horse[i].loc]!=0 and horse[i].finished==False: #start점이나 도착지점에x
            if horse[i].road==road and horse[i].loc==loc:#완전히 같으면
                return False

    return True

def dfs(cnt):
    global sums
    global maxsums
    if cnt==10:
        maxsums=max(maxsums,sums)
        return maxsums


    for i in range(4):
        road=horse[i].road #현재 선로
        loc=horse[i].loc  #현재 선로에서의 위치

        next_road=road #주사위를 굴린후 선로
        next_loc=loc+dice[cnt]  #주사위를 굴린후 선로위에서의 위치

        if horse[i].finished==False:
            if road==0:#외곽 선로
                if next_loc==5:
                    if CheckInHorse(1,0)==True:
                        next_road=1
                        next_loc=0
                        horse[i].road=next_road
                        horse[i].loc=next_loc
                        sums+=rane[next_road][next_loc]
                        dfs(cnt+1)
                        sums-=rane[next_road][next_loc]
                        horse[i].road=road
                        horse[i].loc=loc



                elif next_loc==10:
                    if CheckInHorse(2,0)==True:
                        next_road=2
                        next_loc=0
                        horse[i].road=next_road
                        horse[i].loc=next_loc
                        sums += rane[next_road][next_loc]
                        dfs(cnt+1)
                        sums -= rane[next_road][next_loc]
                        horse[i].road=road
                        horse[i].loc=loc


                elif next_loc==15:
                    if CheckInHorse(3,0)==True:
                        next_road=3
                        next_loc=0
                        horse[i].road=next_road
                        horse[i].loc=next_loc
                        sums += rane[next_road][next_loc]
                        dfs(cnt+1)
                        sums -= rane[next_road][next_loc]
                        horse[i].road=road
                        horse[i].loc=loc

                elif next_loc==20:  #[0][20]은 [4][3]으로
                    if CheckInHorse(4,3)==True:
                        next_road=4
                        next_loc=3
                        horse[i].road=4
                        horse[i].loc=3
                        sums += rane[next_road][next_loc]
                        dfs(cnt+1)
                        sums -= rane[next_road][next_loc]
                        horse[i].road=road
                        horse[i].loc=loc

                else: #그냥 교차로말고 바깥선로에서만 다니면
                    if next_loc>=21: #다음옮긴곳이 도착점이상이면
                        horse[i].finished=True #말 끝남
                        dfs(cnt+1)
                        horse[i].finished=False



                    else: #그냥 선로내에서 움직이면
                        if CheckInHorse(road,next_loc)==True:
                            horse[i].loc=next_loc
                            sums += rane[next_road][next_loc]
                            dfs(cnt+1)
                            sums -= rane[next_road][next_loc]
                            horse[i].loc=loc




            elif road==1 or road==3:
                if next_loc>=4:#이동하는게 그 칸을 넘으면 다음칸으로 지정해줌
                    next_loc=next_loc-4
                    next_road = 4
                    if next_loc>=4:#도착점을넘어가면
                        horse[i].finished=True
                        dfs(cnt+1)
                        horse[i].finished=False
                        continue

                    if CheckInHorse(next_road,next_loc)==True:
                        horse[i].road=next_road
                        horse[i].loc=next_loc
                        sums += rane[next_road][next_loc]
                        dfs(cnt+1)
                        sums -= rane[next_road][next_loc]
                        horse[i].road=road
                        horse[i].loc=loc

                else: #그칸내에서면
                    if CheckInHorse(next_road,next_loc)==True:
                        horse[i].loc=next_loc
                        sums += rane[next_road][next_loc]
                        dfs(cnt+1)
                        sums -= rane[next_road][next_loc]
                        horse[i].loc=loc





            elif road==2:
                if next_loc>=3:
                    next_loc-=3
                    next_road=4
                    if next_loc>=4:
                        horse[i].finished=True
                        dfs(cnt+1)
                        horse[i].finished=False
                        continue

                    if CheckInHorse(next_road,next_loc)==True:
                        horse[i].road=next_road
                        horse[i].loc=next_loc
                        sums += rane[next_road][next_loc]
                        dfs(cnt+1)
                        sums -= rane[next_road][next_loc]
                        horse[i].road=road
                        horse[i].loc=loc

                else:
                    if CheckInHorse(next_road,next_loc)==True:
                        horse[i].loc=next_loc
                        sums += rane[next_road][next_loc]
                        dfs(cnt+1)
                        sums -= rane[next_road][next_loc]
                        horse[i].loc=loc


            elif road==4: #마지막 선로
                if next_loc>=4:#도착지점이후이므로
                    horse[i].finished=True
                    dfs(cnt+1)
                    horse[i].finished=False

                else: #선로내라면
                    if CheckInHorse(next_road,next_loc)==True:
                        horse[i].loc=next_loc
                        sums += rane[next_road][next_loc]
                        dfs(cnt+1)
                        sums -= rane[next_road][next_loc]
                        horse[i].loc=loc







    






sums=0
dice = [0 for _ in range(10)]
rane = [[0 for _ in range(22)] for _ in range(5)]
thorse = [[0 for _ in range(2)] for _ in range(4)]  # horse[i][j] i는 각말 j는 각말의 선로 종류와 그 선로에서의 위치




dice= list(map(int,input().split()))

rane[0][1:21]=[i*2 for i in range(1,21)]
rane[1][:5]=[10,13,16,19,25]
rane[2][:4]=[20,22,24,25]
rane[3][:5]=[30,28,27,26,25]
rane[4][:5]=[25,30,35,40,0]

horse=[Horse(0,0) for _ in range(4)]


maxsums=0
dfs(0)

print(maxsums)













