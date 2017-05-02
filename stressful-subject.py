#help, asap, urgent, or all upper, or ends with 3 exclamation points
import re
#help
re_help = re.compile(r'[hH].*?[eE].*?[lL].*?[pP]')

#asap
re_asap = re.compile(r'[aA].*?[sS].*?[aA].*?[pP]')

#urgent
re_urgent = re.compile(r'[uU].*?[rR].*?[gG].*?[eE].*?[nN].*?[tT]')

def is_stressful(subj):
    if subj[-3:] == '!!!': return True
    subj = ''.join(x for x in subj if x.isalpha())
    if subj.isupper(): return True
    if re.search(re_help, subj) or re.search(re_asap, subj) or re.search(re_urgent, subj): return True
    return False

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    print(is_stressful("Hi") == False)
    print(is_stressful("I neeed HELP") == True)
    print('Done! Go Check it!')
