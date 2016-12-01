def find_message(text):
    f = []
    for x in text:
        if x.isupper():
            f.append(x)
    return ''.join(f)

if __name__ == '__main__':
    print(find_message('How are you? Eh, ok. Low or Lower? Ohhh.'))
    print(find_message('hello world!'))
    print(find_message('HELLO WORLD!!!'))
