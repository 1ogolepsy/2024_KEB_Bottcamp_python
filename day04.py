while True :
    menu = input("1) Fahrenheit -> Celsius  2) Celsius -> Fahrenheit 3) prime number judge \
4) get prime number in range 5) Quit program : ")

    if menu == '1' :

        fahrenheit = float(input("화씨온도 입력 : "))
        print(f'fahrenheit : {fahrenheit}F, Celsius : {(fahrenheit - 32)*(5/9):.2f}')
    elif menu == '2' :
        celsius = float(input("섭씨온도 입력 : "))
        print(f'fahrenheit : {(celsius*(9/5)+32):.4f}F, Celsius : {celsius}')

    elif menu == '3':
        number = int(input('Input number : '))
        is_prime = True

        if number <= 2:
            print(f'{number} is NOT prime number')
        else:
            i = 2

            while i < number:
                if number % i == 0:
                    is_prime = False
                    break
                    # print(i)
                i += 1

            if is_prime:
                print(f'{number} is prime number')
            else:
                print(f'{number} is NOT prime number')

    elif menu == '4':
        numbers = input('First number Second number: ').split()
        n1 = int(numbers[0])
        n2 = int(numbers[1]) + 1

        if n2 < n1:
            n1, n2 = n2, n1

        for number in range(n1, n2):
            if number < 2:
                continue

            is_prime = True

            for i in range(2, number):

                if number % i == 0:
                    is_prime = False
                    break
            if is_prime:
                print(number)

    elif menu == '5':
        print('Terminate Program.')
        break



