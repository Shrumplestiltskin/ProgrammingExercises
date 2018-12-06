def checkio(data):
    return all([any([x for x in data if x.isupper()]), any([x for x in data if x.islower()]), any([x for x in data if x.isdigit()]), len(data) >= 10])

if __name__ == '__main__':
    print(checkio('A1213pokl'))
    print(checkio('bAse730onE4'))
    print(checkio('asasasasasasasaas'))
    print(checkio('QWERTYqwerty'))
    print(checkio('123456123456'))
    print(checkio('QwErTy911poqqqq'))
