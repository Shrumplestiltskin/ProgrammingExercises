#!/usr/bin/python
#Project Eueler #4

#Find the largest palindrome made from the product of two 3-digit numbers

palindrome = 0
for x in xrange(100,999):
    for y in xrange(100,999):
        z = x * y
        if list(str(z))[0] == list(str(z))[-1] and list(str(z))[1] == list(str(z))[-2] and list(str(z))[2] == list(str(z))[-3] and z > palindrome:
            palindrome = z

print(palindrome)
