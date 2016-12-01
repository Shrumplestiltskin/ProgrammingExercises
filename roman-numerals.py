def checkio(data):
    numerals = {1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C', 90:'XC', 50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}
    num_string = ''
    while data:
        for key,value in reversed(sorted(numerals.items())):
            if data >= key:
                num_string += value
                data -= key
                break
    return num_string

if __name__ == '__main__':
    print(checkio(6))
    print(checkio(76))
    print(checkio(13))
    print(checkio(44))
    print(checkio(499))
    print(checkio(3888))
    print(checkio(3999))
