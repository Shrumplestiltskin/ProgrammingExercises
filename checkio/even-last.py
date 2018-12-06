def checkio(array):
    try:
        total = 0
        for x in range(0,len(array),2):
            total += array[x]
        total *= array[-1]
        return total
    except:
        return 0

if __name__ == '__main__':
    print(checkio([0, 1, 2, 3, 4, 5]) == 30)
    print(checkio([1, 3, 5]) == 30)
    print(checkio([6]) == 36)
    print(checkio([]) == 0)
