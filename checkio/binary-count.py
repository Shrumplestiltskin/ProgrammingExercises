def checkio(number):
    return bin(number).count('1')

if __name__ == '__main__':
    print(checkio(4))
    print(checkio(15))
    print(checkio(1))
    print(checkio(1022))
