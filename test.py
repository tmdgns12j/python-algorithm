board=[[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]
def solution(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]==1:
print(solution(board))