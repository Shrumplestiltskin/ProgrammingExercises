def checkio(data, total=0):
    try:
        total += data.pop()
        return checkio(data, total)
    except IndexError: return total


if __name__ == '__main__':
    print(checkio([1,2,3]))
    print(checkio([2,2,2,2,2,2]))
