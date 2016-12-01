def steps_to_convert(line1, line2):
    if len(line2) < len(line1): line1, line2 = line2, line1
    diff = 0
    if line1 in line2: return len(line2) - len(line1)
    for c1, c2 in zip(line1, line2):
        if c1 == c2: pass
        else: diff += 1
    delta = len(line2) - len(line1)
    diff += delta
    return diff

if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    print(steps_to_convert('line1', 'line1'))
    print(steps_to_convert('line1', 'line2'))
    print(steps_to_convert('line', 'line2'))
    print(steps_to_convert('ine', 'line2'))
    print(steps_to_convert('line1', '1enil'))
    print(steps_to_convert('', ''))
    print(steps_to_convert('l', ''))
    print(steps_to_convert('', 'l'))
