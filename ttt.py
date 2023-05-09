
mat = [
    ['x', ' ', 'o'  ]   
    ,['o', 'x', ' ' ]
    ,['o', ' ', 'x' ]
]

def check_valid(mat):
    cx = 0
    co = 0
    for i in range(3):
        cx += mat[i].count('x')
        co += mat[i].count('o')

    if abs(cx - co) > 1:
        return False
    return True
    
def check_win(mat):
    for i in range(3):
        if mat[i][0] == mat[i][1] == mat[i][2] != ' ':
            return mat[i][0]
        if mat[0][i] == mat[1][i] == mat[2][i] != ' ':
            return mat[0][i]
    if mat[0][0] == mat[1][1] == mat[2][2] != ' ':
        return mat[0][0]
    if mat[0][2] == mat[1][1] == mat[2][0] != ' ':
        return mat[0][2]
    return False

print(check_valid(mat))
print(check_win(mat))