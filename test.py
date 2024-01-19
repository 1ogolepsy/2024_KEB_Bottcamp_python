def func(start, end):
    'like range()'
    while start < end:
        yield start
        start += 1

Range = func(1,6)

for i in Range:
    print(i, end=' ')

List = list(Range)
print(List)

