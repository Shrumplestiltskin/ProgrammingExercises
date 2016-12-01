def verify_anagrams(first_word, second_word):
    return True if sorted(first_word.lower().replace(' ', '')) == sorted(second_word.lower().replace(' ', '')) else False

if __name__ == '__main__':
    print(verify_anagrams('Programming', 'Gram Ring Mop'))
    print(verify_anagrams('Hello', 'Ole Oh'))
    print(verify_anagrams('Kyoto', 'Tokyo'))
