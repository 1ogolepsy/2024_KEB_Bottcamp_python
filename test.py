#성능개선 > 1. 4번에서 입력값이 숫자가 하나일 때 등 사용법 안내, 2. 반복되는 것들 함수 3. 화씨가 절대온도 밑으로 내려가는 이슈
#

def isprime(n) -> bool:
    """
    매개변수로 넘겨 받은 수가 소수인지 여부를 boolean으로 리턴
    :param n: 판정할 매개변수
    :return: 소수면 True, 소수가 아니라면 False
    """
    is_prime = True

    if n <= 2:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
             return False
        i += 1
    else:
        return True
while True :
    menu = input("1) Fahrenheit -> Celsius  2) Celsius -> Fahrenheit 3) judge prime number \
4) get prime number in range 5) Quit program : ")

    if menu == '1' :

        fahrenheit = float(input("화씨온도 입력 : "))
        print(f'fahrenheit : {fahrenheit}F, Celsius : {(fahrenheit - 32)*(5/9):.2f}')
    elif menu == '2' :
        celsius = float(input("섭씨온도 입력 : "))
        print(f'fahrenheit : {(celsius*(9/5)+32):.4f}F, Celsius : {celsius}')

    elif menu == '3':
        number = int(input('Input number : '))
        if isprime(number):
            print(f'{number} is prime number')
        else:
            print(f'{number} is NOT prime number')

    elif menu == '4':
        #여기서부터
        numbers = input('First number Second number: ').split()
        n1 = int(numbers[0])
        n2 = int(numbers[1])

        if n2 < n1:
            n1, n2 = n2, n1
        #여기까지 간소화 가능
        for number in range(n1, n2+1):
            if isprime(number):
                print(number, end=' ')

    elif menu == '5':
        print('Terminate Program.')
        break

    else:
        print("유효하지 않은 메뉴입니다.")


