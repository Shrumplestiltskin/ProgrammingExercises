def checkio(expression):
    expression = ''.join([a for a in expression if not a.isdigit() and a not in '+-/*'])
    brackets = ['()', '[]', '{}']
    temp = ''
    while expression is not temp:
        temp = expression
        for bracket in brackets:
            expression = expression.replace(bracket, '')
    return False if expression else True

if __name__ == '__main__':
    print(checkio("((5+3)*2+1)"))
    print(checkio("{[(3+1)+2]+}"))
    print(checkio("(3+{1-1)}"))
    print(checkio("[1+1]+(2*2)-{3/3}"))
    print(checkio("(({[(((1)-2)+3)-3]/3}-3)"))
    print(checkio("2+3"))
