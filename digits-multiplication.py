def checkio(number):
    count = 1
    for a in [x for x in list(map(int, list(str(number)))) if x != 0]:
        count *= a
    return count


if __name__ == '__main__':
    print(checkio(123405))
    print(checkio(999))
    print(checkio(1000))
    print(checkio(1111))
