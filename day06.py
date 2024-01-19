def factorial_repertition(n) -> int:
    '''
    반복문을 이용한 팩토리얼 함수
    :param n: int
    :return: int
    '''
    result = 1
    for i in range(2, n+1):
        result = result* i
    return result

print(factorial_repertition(int(input('number : '))))

def factorial_recursion(n) -> int:
    '''
    재귀함수를 사용한 팩토리얼 함수
    :param n: int
    :return: function, int
    '''

    if n == 1:
        return n
    else:
        return n* factorial_recursion(n-1)

number = int(input('number: '))
print(factorial_recursion(number))