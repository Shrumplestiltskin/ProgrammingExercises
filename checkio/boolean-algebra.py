def boolean(x, y, operation):
    if operation == 'conjunction': return x & y
    if operation == 'disjunction': return x | y
    if operation == 'implication': return (x & y) or not x
    if operation == 'exclusive': return x ^ y
    if operation == 'equivalence': return 1 if x == y else 0


if __name__ == '__main__':
    print(boolean(1, 0, 'conjunction'))
    print(boolean(1, 0, 'disjunction'))
    print(boolean(1, 1, 'implication'))
    print(boolean(0, 1, 'exclusive'))
    print(boolean(0, 1, 'equivalence'))
