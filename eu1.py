answer = []
t = int(input().strip())
for a0 in range(t):
    a = 0
    n = int(input().strip())
    for x in range(0,n):
        if x % 15 == 0 or x % 3 == 0 or x % 5 == 0:
            a += x
    answer.append(a)
for a0 in answer:
    print(a0)
