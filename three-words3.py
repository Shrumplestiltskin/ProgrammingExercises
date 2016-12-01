def checkio(words):
    for pos, word in enumerate([x.isalpha() for x in words.split()]):
        if word and pos + 2 < len(words) and words[pos+1] and words[pos+2]:
            return True
    return False

if __name__ == '__main__':
    print(checkio('Hello World hello'))
    print(checkio('He is 123 man'))
    print(checkio('1 2 3 4'))
    print(checkio('bla bla bla bla'))
    print(checkio('Hi'))
