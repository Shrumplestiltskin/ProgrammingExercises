def translate(phrase):
    import re
    consonant = re.compile('[^aeiouy]+[a|e|i|o|u|y]')
    vowels = re.compile('[a]{3}|[e]{3}|[i]{3}|[o]{3}|[u]{3}|[y]{3}')
    phrase = phrase.split()
    for x in range(len(phrase)):
        t = 0
        for m in consonant.finditer(phrase[x]):
            temp = list(phrase[x])
            if m.start() == 0: phrase[x] = phrase[x][m.start()-t:m.end()-t].replace(m.group(), m.group()[0], 1) + phrase[x][m.end()-t:]
            else: phrase[x] = phrase[x][0:m.start()-t] + phrase[x][m.start()-t:m.end()-t].replace(m.group(), m.group()[0], 1) + phrase[x][m.end()-t:]
            t += 1
    for x in range(len(phrase)):
        for m in vowels.finditer(phrase[x]):
            phrase[x] = phrase[x].replace(m.group(), m.group()[0], 1)
    return ' '.join(phrase)

    
if __name__ == '__main__':
    print(translate("hieeelalaooo"))
    print(translate("hoooowe yyyooouuu duoooiiine"))
    print(translate("aaa bo cy da eee fe"))
    print(translate("sooooso aaaaaaaaa"))
