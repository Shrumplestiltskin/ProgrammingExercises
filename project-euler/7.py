#!/usr/bin/python
#Project Euler #7

#What is the 10001st prime number?

from math import sqrt, floor

def find_prime(x):
    for y in range(2, int(floor(sqrt(x)))+1):
        if x % y == 0:
            return False, x
    return True, x

counter = 2
prime_counter = 0
while True:
    bool_, prime = find_prime(counter)
    if bool_ == True:
        prime_counter += 1
        if prime_counter == 10001:
            print(prime)
            break
    counter += 1
