board=[[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves=[1,5,3,5,1,2,1,4]

def solution(board, moves):
    answer=0
    storage=[]

    cnt=0
    for move in moves:
        for i in range(len(board)):
            if board[i][move-1]!=0:
                storage.append(board[i][move-1])
                board[i][move-1]=0
                break

        if len(storage)>=2:
            if storage[-1]==storage[-2]:
                storage.pop()
                storage.pop()
                cnt+=2







    return cnt

print(solution(board,moves))