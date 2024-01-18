def squares(*n) -> list:
    '''
    넘겨 받은 수치 데이터들의 거듭제곱 값을 리스트에 담아서 리턴
    :param n: tuple
    :return: list
    '''
    return [i*i for i in n]

def run_function(f, *number):
    print(*number)
    return f(*number)

print(run_function(squares,3,4))