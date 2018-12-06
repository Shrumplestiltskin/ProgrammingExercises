#!/usr/bin/python
#Project Euler #10
from math import sqrt, floor
def find_prime(x):
    for y in range(2, int(floor(sqrt(x)))+1):
        if x % y == 0:
            return False
    return True

prime_sum = 0
for count in range (2,2000000):
    bool_ = find_prime(count)
    if bool_ == True:
        prime_sum += count
print(prime_sum)
