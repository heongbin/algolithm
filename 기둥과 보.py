class Node:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.bo=False
        self.gidung=False


def check_correct(m, j, i):  # 현재 기둥이나 보가 제대로된 조건을 갖추는지 확인.
    flag=0
    if  m[i][j].gidung ==True and m[i][j].bo==True:
        if m[i - 1][j].gidung == True or i == 0 or m[i][j - 1].bo == True or m[i][j].bo == True:
            if m[i - 1][j].gidung == True or m[i - 1][j + 1].gidung == True or (m[i][j - 1].bo == True and m[i][j + 1].bo == True):
                return True

    elif m[i][j].gidung ==True and m[i][j].bo==False:
        if m[i - 1][j].gidung == True or i == 0 or m[i][j - 1].bo == True or m[i][j].bo == True:
            return True


    elif m[i][j].bo == True and m[i][j].gidung==False:  # 보
        if m[i - 1][j].gidung == True or m[i - 1][j + 1].gidung == True or (m[i][j - 1].bo == True and m[i][j + 1].bo == True):
            return True

    return False


def solution(n, build_frame):
    answer = []
    m = [[Node(i,j) for j in range(n + 1)] for i in range(n + 1)]
    for i in range(len(build_frame)):
        if build_frame[i][3] == 0: #
            tmp = m[build_frame[i][1]][build_frame[i][0]]
            if build_frame[i][2]==0: #기둥
                m[build_frame[i][1]][build_frame[i][0]].gidung = False
            else:
                m[build_frame[i][1]][build_frame[i][0]].bo = False
            flag = 0
            for k in range(n + 1):
                for t in range(n + 1):
                    if m[k][t].bo==False and m[k][t].gidung==False:
                        continue
                    if check_correct(m, t, k) == False:
                        flag = 1
                        break

                if flag == 1:
                    break
            if flag == 1:
                if build_frame[i][2] == 0:  # 기둥
                    m[build_frame[i][1]][build_frame[i][0]].gidung = True
                else:
                    m[build_frame[i][1]][build_frame[i][0]].bo = True

        elif build_frame[i][3] == 1:  # 설치
            tmp = m[build_frame[i][1]][build_frame[i][0]]
            if build_frame[i][2]==0: #기둥
                m[build_frame[i][1]][build_frame[i][0]].gidung = True
            else:
                m[build_frame[i][1]][build_frame[i][0]].bo = True
            flag = 0
            for k in range(n + 1):
                for t in range(n + 1):
                    if m[k][t].bo == False and m[k][t].gidung == False:
                        continue
                    if check_correct(m, t, k) == False:
                        flag = 1
                        break
                if flag == 1:
                    break
            if flag == 1:
                if build_frame[i][2] == 0:  # 기둥
                    m[build_frame[i][1]][build_frame[i][0]].gidung = False
                else:
                    m[build_frame[i][1]][build_frame[i][0]].bo = False

    for i in range(n + 1):
        for j in range(n + 1):
            if m[i][j].bo == False and m[i][j].gidung == False:
                continue
            if m[i][j].gidung==True:
                answer.append([j, i, 0])
            if m[i][j].bo==True:
                answer.append([j,i,1])

    answer.sort(key=lambda x: (x[0], x[1], x[2]))
    return answer

n=5
build_frame=[[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
print(solution(n,build_frame))