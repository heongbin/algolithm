#정육면체  3*3*3
#윗면: 흰색 , 아랫면: 노란색, 앞면 :빨간색 , 뒷면 :오렌지색 , 왼쪽 : 초록색 , 오른쪽 : 파란색
#U :윗면  ,D : 아랫면, F : 앞면, B : 뒷면, L :왼쪽면 , R : 오른쪽면
#+:시계방향 , -:반시계방향

#       o o o
#       o o o               뒤4       1:초록색 2: 노란색 3: 파란색 4:흰색
#       o o o                        5:오렌지색 6:빨간색
# g g g y y y b b b w w w
# g g g y y y b b b w w w
# g g g y y y b b b w w w  back이랑 down 고침 left고침 right고침
#       r r r
#       r r r               앞5
#       r r r
# 왼      밑    오른  위
# 0       1      2    3
#

color="gybwor"
copycube=[[["" for _ in range(3)] for _ in range(3)] for _ in range(6)]








def counter_clock_direc(num):
    global cube
    tmp=[["" for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            tmp[j][2-i]= cube[num][i][j]

    for i in range(3):
        for j in range(3):
            cube[num][i][j]=tmp[i][j]



def clock_direc(num):
    global cube
    tmp = [["" for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            tmp[2-j][i]=cube[num][i][j]

    for i in range(3):
        for j in range(3):
            cube[num][i][j]=tmp[i][j]


def L_side(direc):
    global cube
    tmpcube = ["" for _ in range(3)]
    if direc=="+": #시계방향일떄 인접한 사이드 배열을 회전
        for i in range(3):
            tmpcube[i]=cube[1][i][0]
        for i in range(3):
            cube[1][i][0]=cube[5][i][0]
        for i in range(3):
            cube[5][i][0]=cube[3][2-i][2]
        for i in range(3):
            cube[3][i][2]=cube[4][2-i][0]
        for i in range(3):
            cube[4][i][0]=tmpcube[i]

    else: #반시계일때 인전합 사이드 배열의 회전
        for i in range(3):
            tmpcube[i]=cube[1][i][0]
        for i in range(3):
            cube[1][i][0]=cube[4][i][0]
        for i in range(3):
            cube[4][i][0]=cube[3][2-i][2]
        for i in range(3):
            cube[3][i][2]=cube[5][2-i][0]
        for i in range(3):
            cube[5][i][0]=tmpcube[i]


def R_side(direc):
    global cube
    tmpcube=["" for _ in range(3)]
    if direc=="+":
        for i in range(3):
            tmpcube[i]=cube[1][i][2]
        for i in range(3):
            cube[1][i][2]=cube[4][i][2]
        for i in range(3):
            cube[4][i][2]=cube[3][2-i][0]
        for i in range(3):
            cube[3][i][0]=cube[5][2-i][2]
        for i in range(3):
            cube[5][i][2]=tmpcube[i]

    else:
        for i in range(3):
            tmpcube[i]=cube[1][i][2]
        for i in range(3):
            cube[1][i][2]=cube[5][i][2]
        for i in range(3):
            cube[5][i][2]=cube[3][2-i][0]
        for i in range(3):
            cube[3][i][0]=cube[4][2-i][2]
        for i in range(3):
            cube[4][i][2]=tmpcube[i]





def f_side(direc):
    global cube
    tmpcube = ["" for _ in range(3)]
    if direc=="+":
        for i in range(3):
            tmpcube[i]=cube[3][2][i]
        for i in range(3):
            cube[3][2][i]=cube[0][2][i]
        for i in range(3):
            cube[0][2][i]=cube[1][2][i]
        for i in range(3):
            cube[1][2][i]=cube[2][2][i]
        for i in range(3):
            cube[2][2][i]=tmpcube[i]

    else:
        for i in range(3):
            tmpcube[i]=cube[3][2][i]
        for i in range(3):
            cube[3][2][i]=cube[2][2][i]
        for i in range(3):
            cube[2][2][i]=cube[1][2][i]
        for i in range(3):
            cube[1][2][i]=cube[0][2][i]
        for i in range(3):
            cube[0][2][i]=tmpcube[i]






def B_side(direc):
    global cube
    tmpcube = ["" for _ in range(3)]
    if direc=="+":
        for i in range(3):
            tmpcube[i] = cube[3][0][i]
        for i in range(3):
            cube[3][0][i]=cube[2][0][i]
        for i in range(3):
            cube[2][0][i]=cube[1][0][i]
        for i in range(3):
            cube[1][0][i]=cube[0][0][i]
        for i in range(3):
            cube[0][0][i]=tmpcube[i]


    else:
        for i in range(3):
            tmpcube[i]=cube[3][0][i]
        for i in range(3):
            cube[3][0][i]=cube[0][0][i]
        for i in range(3):
            cube[0][0][i]=cube[1][0][i]
        for i in range(3):
            cube[1][0][i]=cube[2][0][i]
        for i in range(3):
            cube[2][0][i]=tmpcube[i]

def U_side(direc):
    global cube
    tmpcube = ["" for _ in range(3)]
    if direc == "+":
        for i in range(3):
            tmpcube[i]=cube[4][0][i]
        for i in range(3):
            cube[4][0][i]=cube[0][2-i][0]
        for i in range(3):
            cube[0][i][0]=cube[5][2][i]
        for i in range(3):
            cube[5][2][i]=cube[2][2-i][2]
        for i in range(3):
            cube[2][i][2]=tmpcube[i]

    else:
        for i in range(3):
            tmpcube[i]=cube[4][0][i]
        for i in range(3):
            cube[4][0][i]=cube[2][i][2]
        for i in range(3):
            cube[2][i][2]=cube[5][2][2-i]
        for i in range(3):
            cube[5][2][i]=cube[0][i][0]
        for i in range(3):
            cube[0][i][0]=tmpcube[2-i]

def D_side(direc):
    global cube
    tmpcube = ["" for _ in range(3)]
    if direc == "+":
        for i in range(3):
            tmpcube[i]=cube[4][2][i]
        for i in range(3):
            cube[4][2][i]=cube[2][i][0]
        for i in range(3):
            cube[2][i][0]=cube[5][0][2-i]
        for i in range(3):
            cube[5][0][i]=cube[0][i][2]
        for i in range(3):
            cube[0][i][2]=tmpcube[2-i]

    else:
        for i in range(3):
            tmpcube[i]=cube[4][2][i]
        for i in range(3):
            cube[4][2][i]=cube[0][2-i][2]
        for i in range(3):
            cube[0][i][2]=cube[5][0][i]
        for i in range(3):
            cube[5][0][i]=cube[2][2-i][0]
        for i in range(3):
            cube[2][i][0]=tmpcube[i]











T=int(input()) #테스트 개수

for test_case in range(T):
    cube=copycube[:]
    for i in range(6):
        for j in range(3):
            for k in range(3):
                cube[i][j][k] = color[i]

    number_rotate = int(input()) #회전수
    rotate_direc= list(map(str,input().split()))

    for rotate in rotate_direc:
        if rotate[0]=="L":
            if rotate[1]=="+":
                clock_direc(0)
                L_side(rotate[1])
            elif rotate[1]=="-":
                counter_clock_direc(0)
                L_side(rotate[1])
        elif rotate[0]=="R":
            if rotate[1]=="+":
                clock_direc(2)
                R_side(rotate[1])
            elif rotate[1]=="-":
                counter_clock_direc(2)
                R_side(rotate[1])
        elif rotate[0]=="F":
            if rotate[1]=="+":
                clock_direc(5)
                f_side(rotate[1])
            elif rotate[1]=="-":
                counter_clock_direc(5)
                f_side(rotate[1])
        elif rotate[0]=="B":
            if rotate[1]=="+":
                clock_direc(4)
                B_side(rotate[1])
            elif rotate[1]=="-":
                counter_clock_direc(4)
                B_side(rotate[1])
        elif rotate[0]=="U":
            if rotate[1]=="+":
                clock_direc(3)
                U_side(rotate[1])
            elif rotate[1]=="-":
                counter_clock_direc(3)
                U_side(rotate[1])
        elif rotate[0]=="D":
            if rotate[1]=="+":
                clock_direc(1)
                D_side(rotate[1])
            elif rotate[1]=="-":
                counter_clock_direc(1)
                D_side(rotate[1])


    for i in range(3):
        print("{}{}{}".format(cube[3][i][2],cube[3][i][1],cube[3][i][0]))

