#!/usr/bin/python
#Project Eueler #9

for x in range(1,1000):
    for y in range(1,1000):
        for z in range(1,1000):
            if x < y < z:
                if ((x ** 2) + (y ** 2) == (z ** 2)) and ((x + y + z) == 1000):
                    print(x * y * z)
                    exit(0)
