def checkio(str_number, radix):
    try: return int(str_number, radix)
    except ValueError: return -1

if __name__ == '__main__':
    print(checkio('AF', 16))
    print(checkio('101', 2))
    print(checkio('101', 5))
    print(checkio('Z', 36))
    print(checkio('AB', 10))
