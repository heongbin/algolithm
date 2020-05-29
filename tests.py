import copy

def solution(key,lock):
    entire_lock = [[0 for _ in range(len(lock)*3)] for _ in range(len(lock)*3)]
    for i in range(len(lock),len(lock)*2):
        for j in range(len(lock),len(lock)*2):
            entire_lock[i-len(lock)][j-len(lock)]=lock[i][j]


    move(lock,entire_lock)

    return entire_lock


def rotate(lock):
    n=len(lock)
    tmp=[[0 for _ in range(len(lock))] for _ in range(len(lock))]
    for i in range(len(lock)):
        for j in range(len(lock[i])):
            tmp[j][n-1-i] = lock[i][j]

    return tmp



def move(m,copy_lock):
    n=len(m)
    for kr in range(3*n):
        for kc in range(3*n):
            copy_lock
            for i in range(n):
                for j in range(n):
                    copy_lock[i+kr][j+kc]=m[i][j]

            print(copy_lock)


# 1 1 1 (0,0)->(0,2)/ (0,1)->(1,2)/(0,2)->(2,2) (i,j)
# 1 1 0
# 1 0 1

# 1 0 1
# 0 1 1
# 1 1 1

lock=[[1, 1, 1], [1, 1, 0], [1, 0, 1]]
key=[[0, 0, 0], [1, 0, 0], [0, 1, 1]]

# 0 0 0
# 1 0 0
# 0 1 1

#

print(rotate(key))








