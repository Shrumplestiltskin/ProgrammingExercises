from numpy import array
def checkio(matrix):
    #matrix = array([x for y in matrix for x in y])
    #matrix = array(matrix)
    return True if (array(matrix).transpose() == -array(matrix)).all() else False

if __name__ == '__main__':
    print(checkio([[0,1,2],[-1,0,1],[-2,-1,0]]))
    print(checkio([[0,1,2],[-1,1,1],[-2,-1,0]]))
    print(checkio([[0,1,2],[-1,0,1],[-3,-1,0]]))
    print(checkio([[ 0, 1, 2, 3, 4], 
                   [-1, 0, 5, 6, 7], 
                   [-2,-5, 0, 8, 9], 
                   [-3,-6,-8, 0, 0], 
                   [-4,-7,-9, 0, 0]]))
