def largest_histogram(histogram):
    maxarea = 0
    for x in range(len(histogram)):
        min=histogram[x]
        for y in range(x, len(histogram)):
            if histogram[y] < min: min = histogram[y]
            if min*(y-x+1) > maxarea: maxarea = min*(y-x+1)
    return maxarea


if __name__ == '__main__':
    print(largest_histogram([5]))
    print(largest_histogram([5,3]))
    print(largest_histogram([1,1,4,1]))
    print(largest_histogram([1,1,3,1]))
    print(largest_histogram([2,1,4,5,1,3,3]))
