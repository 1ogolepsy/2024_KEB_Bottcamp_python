#9.16.1
def good() -> list:
    '''
    chapter 0 things to do. 91.
    :return: list
    '''
    movie = input('Harry, Ron, Hermione를 입력하세요. :')
    Harry_poter = movie.split(', ')
    return Harry_poter

print(good())

#9.16.2
def get_odds(n) -> int:
    '''
    1부터 n까지의 홀수를 발생시키는 제너레이터
    :param n: int
    :return: int
    '''
    odd_num = []
    for i in range(1, n+1, 2):
        yield i

for j in get_odds(10):
    print(j, end=' ')

#9.16.3
def test(function):
    '''
    데코레이터 함수, 함수 시작하면 start 출력, 함수 끝나면 end 출력
    :param function: func
    :return: closer func
    '''
    def decoration(*args, **kwargs):
        print('start')
        a = function(*args, **kwargs)
        print('end')
        return a
    return decoration
#
# def test(func):
#     print('start')
#     a = func()
#     print('end')
#     return a
@test
def OriginalFunc():
    print('프로그램이 실행되었습니다.')
    return print('프로그램이 끝났습니다.')

OriginalFunc()
#9.16.4
class OopsException(Exception):
    # print('숫자를 입력하지 않았습니다. 프로그램을 종료합니다.')
    pass

num = input("숫자를 입력하세요. : ")
try:
    print(num)
    if num != int:
        raise OopsException(num)
except OopsException as Oops:
    print('숫자를 입력하지 않았습니다. 프로그램을 종료합니다.')