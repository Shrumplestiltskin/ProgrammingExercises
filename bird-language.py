VOWELS = "aeiouy"

def translate(phrase):
    for x in range(len(list(phrase))):
        if phrase[x] not in VOWELS and phrase[x]+1 in VOWELS:
    
if __name__ == '__main__':
    print(translate("hieeelalaooo"))
    print(translate("hoooowe yyyooouuu duoooiiine"))
    print(translate("aaa bo cy da eee fe"))
    print(translate("sooooso aaaaaaaaa"))
