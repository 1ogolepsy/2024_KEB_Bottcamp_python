def squares(n):
    return n*n

even_number = [i for i in range(51) if i % 2 == 0]
print(even_number)
print(tuple(map(squares, even_number)))

print(tuple(map(lambda x : x**2, even_number)))