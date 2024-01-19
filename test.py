def Original_func(n1, n2):
    if n1 and n2 is True:
        print('do something')

def decoration(func):
    def inner(*args):
        print('start')
        print(args)
        print(*args)
        func(*args)
        print('end')
    return inner

test = decoration(Original_func)

test(3, 4)