def decoration(func):
    def inner(*args):
        print('start')
        print(args)
        print(*args)
        func(*args)
        print(n3)
        print('end')
    return inner


@decoration
def Original_func(n1, n2):
    if n1 and n2 is True:
        n3 = 'Original 지역변수'
        print('do something')


Original_func(1, 3)
