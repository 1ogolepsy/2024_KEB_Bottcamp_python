# subject = {'python' : 'ken', 'c++':'sung','data structure':'kim','database':'kang'}
# print("{0[python]} {0[database]}".format(subject))

numbers = input('First number Second number: ').split()
n1 = int(numbers[0])
n2 = int(numbers[1])+1

if n2 < n1:
    n1, n2 = n2, n1

for number in range(n1, n2):
    if number < 2:
        continue

    is_prime = True

    for i in range(2,number):

        if number % i == 0:
            is_prime = False
            break
    if is_prime:
        print(number)

