def checkio(marbles, step):
    from operator import countOf
    b = countOf(marbles, 'b')
    w = countOf(marbles, 'w')



if __name__ == '__main__':
    print(checkio('bbw', 3))
    print(checkio('wwb', 3))
    print(checkio('www', 3))
    print(checkio('bbbb', 1))
    print(checkio('wwbb', 4))
    print(checkio('bwbwbwb', 5))
