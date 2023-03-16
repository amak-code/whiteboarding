# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need 
# to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 
# 1-9 without repetition.

# Note:
# A Sudoku board (partially filled) could be valid but is not necessarily 
# solvable.
# Only the filled cells need to be validated according to the mentioned rules.
 

def valid_sudoku(board):

    rows = [set() for _ in range(9)]
    columns = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]


    for i in range(9):
        for j in range(9):
            val = board[i][j]
            if val == ".":
                continue

            else:
                if val in rows[i] or val in columns[j] or val in boxes[(i//3)*3 + j//3]:

                    return False
                else:
                    rows[i].add(val)
                    columns[j].add(val)
                    boxes[(i//3)*3 + j//3].add(val)


    return True




board =[["8","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]

print(valid_sudoku(board))