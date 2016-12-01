arr = list(map(int, input().split()))
t = int(input())
if t > len(arr)-1:
    print(-1)
else:
    print(arr[t] ** t)
