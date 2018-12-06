def checkio(data):
    return [x for x in data if data.count(x) > 1]

if __name__ == '__main__':
    print(checkio([1,2,3,1,3]))
    print(checkio([1,2,3,4,5]))
    print(checkio([5,5,5,5,5]))
    print(checkio([10,9,10,10,9,8]))
