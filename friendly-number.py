def friendly_number(number, base=1000, decimals=0, suffix='', powers=['', 'k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y']):
    power = list(powers)
    while abs(number) >= base and len(power) > 1: 
        number /= base
        power.pop(0)
    if decimals and float(number) % 1 == 0.0: #This is so stupid
        decimal = ''
        for x in range(decimals-1): decimal += '0'
        return str(float(number)) + decimal + power[0] + suffix
    if str(number).replace('.', '') == len(str(number).replace('.', '')) * str(number)[0]: return str(int(round(number))) + power[0] + suffix
    return str(round(number, decimals)) + str(power[0]) + str(suffix) if decimals else str(int(number)) + str(power[0]) + str(suffix)

    



if __name__ == '__main__':
    print(friendly_number(102, decimals=2))
    print(friendly_number(10240))
    print(friendly_number(12341234, decimals=1))
    print(friendly_number(12461, decimals=1))
    print(friendly_number(1024000000, base=1024, suffix='iB'))
    print(friendly_number(12000000, decimals=3))
    print(friendly_number(-150, base=100, powers=['', 'd', 'D']))
    print(friendly_number(255000000000, powers=["","k","M"]))
    print(friendly_number(10**32))
