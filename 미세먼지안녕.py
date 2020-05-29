import copy
def check_range(x,y):
    if x<0 or y<0 or x>=M or y>=N:
        return False
    return True
def chcek_minus():
    for i in range(M):
        for j in range(N):
            if i==0 and j==up_air_clr_y:
                continue
            if i==0 and j==down_air_clr_y:
                continue
            if m[j][i]<0:
                m[j][i]=0

def spread_dust(x,y):
    if m[y][x]>0:

        count_spread=0 #확산된 칸수 세기
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if check_range(nx,ny)==False:
                continue
            if m[ny][nx]==-1: #공기청정기가 있는곳
                continue
            tmp_m[ny][nx]+=m[y][x]//5
            count_spread+=1

        m[y][x]-=count_spread*(m[y][x]//5)


def run_upper_airclner(x,y):
    copy_down_row=m[y][:]
    down_row_last=copy_down_row.pop()
    copy_down_row.insert(0,-1)

    copy_right_col=[0 for _ in range(y)]
    for i in range(y):
        copy_right_col[i]=m[i][M-1]
    right_col_last=copy_right_col.pop(0)
    copy_right_col.append(down_row_last)

    copy_up_row=m[0][:M-1]
    up_row_last=copy_up_row.pop(0)
    copy_up_row.append(right_col_last)

    copy_left_col=[0 for _ in range(y-1)]
    for i in range(1,y):
        copy_left_col[i-1]=m[i][0]
    copy_left_col.insert(0,up_row_last)
    copy_left_col.pop()

    m[y]=copy_down_row[:]
    for i in range(y):
        m[i][M-1]=copy_right_col[i]
    m[0][:M-1]=copy_up_row[:]
    for i in range(1, y):
        m[i][0]=copy_left_col[i - 1]










def run_under_airclner(x,y):
    copy_up_row = m[y][:]
    up_row_last = copy_up_row.pop()
    copy_up_row.insert(0,-1)

    copy_right_col=[0 for _ in range(N-(y+1))]
    for i in range(y+1,N):
        copy_right_col[i-(y+1)]=m[i][M-1]
    right_col_last = copy_right_col.pop()
    copy_right_col.insert(0,up_row_last)

    copy_down_row = m[N-1][:M-1]
    down_row_last = copy_down_row.pop(0)
    copy_down_row.append(right_col_last)

    copy_left_col=[0 for _ in range((N-1)-(y+1))]
    for i in range(y+1,N-1):
        copy_left_col[i-(y+1)]=m[i][0]
    copy_left_col.pop(0)
    copy_left_col.append(down_row_last)

    m[y] = copy_up_row[:]
    for i in range(y+1,N):
        m[i][M-1]=copy_right_col[i-(y+1)]
    m[N-1][:M-1] = copy_down_row[:]
    for i in range(y+1,N-1):
        m[i][0]=copy_left_col[i-(y+1)]


dx=[-1,1,0,0]
dy=[0,0,1,-1]
N,M,T = map(int,input().split())

#행 열 타임

m=[[0 for _ in range(M)] for _ in range(N)]
for i in range(N):
    m[i]=list(map(int,input().split()))

up_air_clr_y = 0
down_air_clr_y = 0
for i in range(N):
    if m[i][0]==-1:
        up_air_clr_y=i
        down_air_clr_y=i+1
        break

for t in range(T):
    tmp_m=[[0 for _ in range(M)] for _ in range(N)]
    for i in range(M):
        for j in range(N):
            spread_dust(i,j)

    for i in range(M):
        for j in range(N):
            m[j][i]+=tmp_m[j][i]



    run_upper_airclner(0,up_air_clr_y)
    run_under_airclner(0,down_air_clr_y)
    chcek_minus()


sums=0
for i in range(N):
    for j in range(M):
        if m[i][j]>0:
            sums+=m[i][j]

print(sums)


