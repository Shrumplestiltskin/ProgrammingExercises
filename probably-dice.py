from itertools import permutations
import operator
from collections import Counter
from math import factorial
from functools import reduce
def sum_to_n(n, size, limit=None):
    if size == 1:
        yield [n]
        return
    if limit is None:
        limit = n
    start = (n + size - 1) // size
    stop = min(limit, n - size + 1) + 1
    for i in range(start, stop):
        for tail in sum_to_n(n - i, size - 1, i):
            yield [i] + tail

def npermutations(l):
    num = factorial(len(l))
    mults = Counter(l).values()
    den = reduce(operator.mul, (factorial(v) for v in mults), 1)
    return num / den

def probability(num_dice, num_sides, number_to_hit):
    if num_dice * num_sides < number_to_hit or number_to_hit == 0 : return 0
    a = []
    for x in sum_to_n(number_to_hit, num_dice, limit=num_sides):
        a.append(x)
    total = 0
    for x in a:
        total += npermutations(x)
            
    return float('{0:.4f}'.format(total / (num_sides ** num_dice)))

if __name__ == '__main__':
    #print(probability(2, 6, 3))
    #print(probability(2, 6, 4))
    #print(probability(2, 6, 7))
    #print(probability(2, 3, 5))
    #print(probability(2, 3, 7))
    #print(probability(3, 6, 7))
    #print(probability(10, 10, 50))
    print(probability(1, 2, 999)) #0

    #Probability of rolling n x sided dice for n is 1 / x ** n
    #So for instance to roll a 3 with a six sided dice, it is 1 / 6 ** 3 or 1/216

    #To find the probability of rolling a 4 for instance, you must take the ways to make a four
    #In this case 1+1+2, 1+2+1, 2+1+1 .....that equals 3/216
    #Likewise for 7 - 
    #1 + 1 + 5, 1 + 5 + 1, 5 + 1 + 1 = 3
    #1 + 2 + 4, 1 + 4 + 2, 4 + 1 + 2, 4 + 2 + 1, 2 + 4 + 1, 2 + 1 + 4 = 6
    #3 + 2 + 2, 2 + 3 + 2, 2 + 2 + 3 = 3
    #3 + 3 + 1, 3 + 1 + 3, 1 + 3 + 3 = 3
    # = 15/216

    #So the question becomes, how to efficiently retrieve all permutations
