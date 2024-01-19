#9.16.1
def good():
    return ['Harry', 'Ron', 'Hermione']

#9.16.2
def get_odds():
    odd_num = []
    for i in range(10):
        if i % 2 != 0:
            odd_num += [i]
    return odd_num
print(get_odds())
#9.16.3
def test(function):
    print('start')
    a = function()
    print('end')
    return a

def OriginalFunc():
    print('프로그램이 실행되었습니다.')
    return print('프로그램이 끝났습니다.')

test(OriginalFunc)

#9.16.4
class OopsException(Exception):
    print('숫자를 입력하지 않았습니다. 프로그램을 종료합니다.')

num = input("숫자를 입력하세요. : ")
try:
    print(num)
    if num != int:
        raise OopsException(num)
except OopsException as Oops:
    print('숫자를 입력하지 않았습니다. 프로그램을 종료합니다.')