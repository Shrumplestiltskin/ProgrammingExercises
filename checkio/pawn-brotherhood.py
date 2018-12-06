def safe_pawns(pawns):
    return len([x for x in pawns if chr(ord(x[0]) - 1) + str(int(x[1])-1) in pawns or chr(ord(x[0])+1) + str(int(x[1])-1) in pawns])

if __name__ == '__main__':
    print(safe_pawns({'b4', 'd4', 'f4', 'c3', 'e3', 'g5', 'd2'}))
    print(safe_pawns({'b4', 'c4', 'd4', 'e4', 'f4', 'g4', 'e5'}))
