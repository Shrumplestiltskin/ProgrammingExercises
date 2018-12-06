#!/usr/bin/python3
#Project Euler #2
#sum of even fibo terms whose values do not exceed 4M

x = 0
y = 1
total = 0
while x < 4000000:
    temp = x
    x = x + y
    y = temp
    if x % 2 == 0:
        total += x
print(total)

