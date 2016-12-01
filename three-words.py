def checkio(words):
    count = 0
    for x in words.split():
        if x.isalpha():
            count += 1
            if count == 3: return True
        else: count = 0
    return False

if __name__ == '__main__':
    print(checkio('Hello World hello'))
    print(checkio('He is 123 man'))
    print(checkio('1 2 3 4'))
    print(checkio('bla bla bla bla'))
    print(checkio('Hi'))
