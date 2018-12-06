#!/usr/bin/python
#Project Eueler #6

a, b, x, y = 0, 0, 0, 0
for x in range(1,101):
    a += (x ** 2)
for y in range(1,101):
    b += y
print((b**2) - a)
