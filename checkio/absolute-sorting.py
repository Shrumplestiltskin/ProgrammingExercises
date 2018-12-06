def checkio(numbers_array):
    return sorted(numbers_array, key=abs)

if __name__ == '__main__':
    print(checkio((-20,-5,10,15)))
    print(checkio((1,2,3,0)))
    print(checkio((-1,-2,-3,0)))
