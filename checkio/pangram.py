def check_pangram(text):
    alpha = set()
    return True if len([x for x in text.lower() if x.isalpha() and x not in alpha and alpha.add(x) is None]) == 26 else False

if __name__ == '__main__':
    print(check_pangram("The quick brown fox jumps over the lazy dog."))
    print(check_pangram("ABCDEF"))
    print(check_pangram("Bored? Craving a pub quiz fix? Why, just come to the Royal Oak!"))
    print(check_pangram('abcdefghijklmnopqrstuvwxyz'))
