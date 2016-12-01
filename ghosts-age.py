def checkio(opacity):
    def fibo(n): return n if n <= 1 else (fibo(n-1) + fibo(n-2))
    fibarr = ([fibo(a) for a in range(0,20)])
    year, opac, ghost_arr = 1, 10000, [10000]
    while opacity not in ghost_arr:
        opac = opac - year if year in fibarr else opac + 1
        year += 1
        ghost_arr.append(opac)
    return ghost_arr.index(opacity)

if __name__ == '__main__':
    print(checkio(10000)) #0
    print(checkio(9999))  #1
    print(checkio(9997))  #2
    print(checkio(9994))  #3
    print(checkio(9995))  #4
    print(checkio(9990))  #5
