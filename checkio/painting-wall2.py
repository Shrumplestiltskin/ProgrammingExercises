#just store beginnings and ends
def checkio(required, operations):
    range_collection = []

    if sorted(operations,key = lambda x: int(x[1]))[-1][1] < required: return -1
    for x in range(len(operations)):
        total = 0
        start = operations[x][0]
        end = operations[x][1] + 1

        for y in range(len(range_collection)):
            if start in range(range_collection[y][0], range_collection[y][1]+1):
                range_collection[y][1] = (end - 1)
            elif end in range(range_collection[y][0], range_collection[y][1]+1):
                range_collection[y][0] = start
            else:
                range_collection.append([start, end-1])

        for a in range(len(range_collection)):
            total += (range_collection[a][1] + 1) - range_collection[a][0]
        if total >= required: return len(range_collection)

    return -1


            #need to check if 
        







if __name__ == '__main__':
    print(checkio(5, [[1, 5], [11, 15], [2, 14], [21, 25]]))
    print(checkio(6, [[1, 5], [11, 15], [2, 14], [21, 25]]))
    print(checkio(11, [[1, 5], [11, 15], [2, 14], [21, 25]]))
    print(checkio(16, [[1, 5], [11, 15], [2, 14], [21, 25]]))
    print(checkio(21, [[1, 5], [11, 15], [2, 14], [21, 25]]))
    print(checkio(1000000011, [[1, 1000000000], [11, 1000000010]]))


#figure out how many integers are in the range
#range[1]+1 - range[0]
