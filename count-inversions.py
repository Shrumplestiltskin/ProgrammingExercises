def count_inversion(sequence):
    sequence = list(sequence)
    count = 0
    for x in range(len(sequence)):
            for y in range(x+1,len(sequence)):
                if sequence[x] > sequence[y]:
                    count += 1
                    sequence[x],sequence[y] = sequence[y],sequence[x]
    return count
    

if __name__ == '__main__':
    print(count_inversion((1,2,5,3,4,7,6)))
    print(count_inversion((0,1,2,3)))
    print(count_inversion((99,-99)))
    print(count_inversion((5,3,2,1,0)))
