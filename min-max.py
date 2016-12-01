def isgenerator(iterable):
    return (hasattr(iterable,'__iter__') and not hasattr(iterable,'__len__')) or type(iterable) == range

def min(*args, **kwargs):
    key = kwargs.get('key', None)
    if isgenerator(args[0]): args = args[0]
    try:
        if len(args) == 1: args = type(args[0])(args[0])
    except TypeError:
        pass
    return sorted(args, key=key)[0]

def max(*args, **kwargs):
    key = kwargs.get('key', None)
    if isgenerator(args[0]): args = args[0]
    try:
        if len(args) == 1: args = type(args[0])(args[0])
    except TypeError:
        pass
    return sorted(args, key=key, reverse=True)[0]

if __name__ == '__main__':
    print(max(3,2))
    print(min(3,2))
    print(max([1,2,0,3,4]))
    print(min('hello'))
    print(max(2.2,5.6,5.9,key=int))
    print(min([1,2],[3,4],[9,0], key=lambda x:x[1]))
    print(max(range(6)))
    print(min(abs(i) for i in range(-10, 10)))
