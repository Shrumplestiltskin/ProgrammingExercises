def longest_palindromic(text):
    return text if text == ''.join(reversed(text)) else max([text[x:y:] for x in range(len(text)) for y in range(len(text)) if text[x:y:] == ''.join(reversed(text[x:y:]))], key=len)

if __name__ == '__main__':
    print(longest_palindromic('artrartrt'))
    print(longest_palindromic('abacada'))
    print(longest_palindromic('aaaa'))
    print(longest_palindromic('aaaaa'))
