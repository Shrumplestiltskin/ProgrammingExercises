def checkio(data):
    from statistics import median
    return median(data)

if __name__ == '__main__':
    print(checkio([1,2,3,4,5]))
    print(checkio([3,1,2,5,3]))
    print(checkio([1,300,2,200,1]))
    print(checkio([3,6,20,99,10,15]))
    print(checkio(list(range(1000000))))
