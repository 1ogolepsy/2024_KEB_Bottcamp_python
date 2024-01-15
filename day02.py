# temp = [0]
# if temp:
#     print("원소가 존재")
# else :
#     print("비어있는 리스트")


menu = input("1) Fahrenheit -> Celsius  2) Celsius -> Fahrenheit  3) Quit program : ")

if menu == '1' :

    fahrenheit = float(input("화씨온도 입력 : "))
    print(f'fahrenheit : {fahrenheit}F, Celsius : {(fahrenheit - 32)*(5/9):.2f}')
elif menu == '2' :
    celsius = float(input("섭씨온도 입력 : "))
    print(f'fahrenheit : {(celsius*(9/5)+32):.4f}F, Celsius : {celsius}')
else :
    print('Terminate Program.')
# print(int('1A', 16))

