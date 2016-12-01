from math import degrees, acos
def checkio(a,b,c):
    try:
        dega = round(degrees(acos((b**2 + c**2 - a**2) / (2 * b * c))))
        degb = round(degrees(acos((c**2 + a**2 - b**2) / (2 * c * a))))
        return sorted([dega,degb,180 - dega - degb]) if dega and degb else [0,0,0]
    except ValueError:return [0,0,0]

if __name__ == '__main__':
    print(checkio(4,4,4))
    print(checkio(3,4,5))
    print(checkio(2,2,5))
