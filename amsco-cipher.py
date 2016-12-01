def decode_amsco(message, key):
    temp = len(str(key))

def encode_amsco(message, key):
    #get amount of numbers in key 
    temp = len(str(key))
    a = list(message)
    #to figure if list index is odd or even
    str(key).index('num') % 2 == 0


if __name__ == '__main__':
    print(decode_amsco('oruoreemdstmioitlpslam', 4123))
    print(decode_amsco('kicheco', 23415))
    print(decode_amsco('hrewhoorrowyilmmmoaouletow', 123))





'''
kicheco 23415

2   3   4   1   5
c   he  c  ki   o


hrewhoorrowyilmmmoaouletow 123

1           2           3
h           ow          a
re          y           ou
w           il          l
ho          m           et
o           mm          o
rr          o           w

oruoreemdstmioitlpslam 4123       round(len(string)/len(string(4123))) == 6


4       1       2       3
l       or      e       mi
ps      u       md      o
l       or      s       it
am      e       t
'''
