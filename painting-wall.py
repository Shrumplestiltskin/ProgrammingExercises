from operator import itemgetter
from itertools import groupby

def checkio(required, operations):
    #if sorted(operations,key = lambda x: int(x[1]))[-1][1] < required: return -1
    operations = [range(x[0], x[1] + 1) for x in operations]
    used_numbers,count = [], 0

    for x in operations:
        temp = []
        total = 0
        if not used_numbers: used_numbers.append(x)

        #this is where it chokes
        temp_ranges = list(used_numbers)
        found = False
        while not found:
            for z in temp_ranges:
                if x.start >= z.start and x.stop <= z.stop:
                    #operation range fits inside preexisting range
                    #if this happens no action should be performed
                    found = True
                elif z.start >= x.start and z.stop <= x.stop:
                    #preexisting range fits within an operation range
                    #if this happens the range should be removed from the used_numbers list and the new range should be appended


                elif x.start < z.start and x.stop >= z.start and x.stop <= z.stop:
                    #range extends an existing range leftwards, the end fitting inside a preexisting range
                    temp.append(


        '''
        for y in x:
            print(y)
            temp_ranges = list(used_numbers)
            found = False
            for z in temp_ranges: #iterates through ranges and appends any loose integers
                if y in z:
                    _ = 0
                    found = True
            if found == False: temp.append(y)
        '''

        #builds new ranges based off of loose ints and appends to original list
        for k, g in groupby(enumerate(temp), lambda ix: ix[0] - ix[1]):
            group = list(map(itemgetter(1), g))
            used_numbers.append(range(group[0], group[-1]))

        for f in used_numbers:
            total += (f.__len__())
        count += 1
        if total >= required: return count

    return -1


if __name__ == '__main__':
    #print(checkio(5, [[1, 5], [11, 15], [2, 14], [21, 25]]))
    #print(checkio(6, [[1, 5], [11, 15], [2, 14], [21, 25]]))
    #print(checkio(11, [[1, 5], [11, 15], [2, 14], [21, 25]]))
    #print(checkio(16, [[1, 5], [11, 15], [2, 14], [21, 25]]))
    #print(checkio(21, [[1, 5], [11, 15], [2, 14], [21, 25]]))

    #this one fails
    #print(checkio(30, [[1, 2], [20, 30], [25, 28], [5, 10], [4, 21], [1, 6]]))

    print(checkio(1000000011, [[1, 1000000000], [11, 1000000010]]))


#ranges can be kept in tuple
#range.__len__() returns length



#ranges = []
#for k, g in groupby(enumerate(data), lambda ix: ix[0] - ix[1]):
#    group = list(map(itemgetter(1), g))
#    ranges.append((group[0], group[-1]))

