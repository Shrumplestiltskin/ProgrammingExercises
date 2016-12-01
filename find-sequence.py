def checkio(matrix):
    vert = [matrix[x][y] for x in range(len(matrix)-3) for y in range(len(matrix[x])) if matrix[x][y] == matrix[x+1][y] == matrix[x+2][y] == matrix[x+3][y]]
    horiz = [matrix[x][y] for x in range(len(matrix)) for y in range(len(matrix[x])-3) if matrix[x][y] == matrix[x][y+1] == matrix[x][y+2] == matrix[x][y+3]]
    fdiag = [matrix[x][y] for x in range(len(matrix)-3) for y in range(3,len(matrix[x])) if matrix[x][y] == matrix[x+1][y-1] == matrix[x+2][y-2] == matrix[x+3][y-3]]
    rdiag = [matrix[x][y] for x in range(len(matrix)-3) for y in range(len(matrix[x])-3) if matrix[x][y] == matrix[x+1][y+1] == matrix[x+2][y+2] == matrix[x+3][y+3]]
    return True if vert or horiz or fdiag or rdiag else False

if __name__ == '__main__':
    print(checkio([[1,2,1,1],
                   [1,1,4,1],
                   [1,3,1,6],
                   [1,7,2,5]]))
    print(checkio([[7,1,4,1],
                   [1,2,5,2],
                   [3,4,1,3],
                   [1,1,8,1]]))
    print(checkio([[2,1,1,6,1],
                   [1,3,2,1,1],
                   [4,1,1,3,1],
                   [5,5,5,5,5],
                   [1,1,3,1,1]]))
    print(checkio([[7,1,1,8,1,1],
                   [1,1,7,3,1,5],
                   [2,3,1,2,5,1],
                   [1,1,1,5,1,4],
                   [4,6,5,1,3,1],
                   [1,1,9,1,2,1]]))
    print(checkio([[1,5,4,4],
                   [2,2,4,1],
                   [1,4,3,5],
                   [4,3,3,2]]))
    print(checkio([[6,9,1,1,6,2],
                   [5,9,7,8,2,5],
                   [2,1,1,7,9,8],
                   [1,8,1,4,7,4],
                   [7,8,5,4,5,1],
                   [6,4,8,8,1,8]]))
    print(checkio([[1,9,7,8,9,3,6,5,6,2],
                   [4,9,4,8,3,4,8,8,5,9],
                   [2,8,5,5,7,8,6,1,3,6],
                   [6,4,7,6,9,1,4,5,7,8],
                   [4,7,7,9,8,8,8,8,4,4],
                   [3,7,3,2,1,9,1,8,9,1],
                   [4,7,2,4,8,1,2,3,6,2],
                   [4,4,1,3,3,3,9,2,6,7],
                   [8,6,1,9,3,5,8,1,7,5],
                   [7,3,6,5,3,6,6,4,8,2]]))
