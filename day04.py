import copy
subject = ['a', ['b', 'c'], 'd',]
a = subject
b = subject.copy()
c = list(subject)
d = subject[:]
e = copy.deepcopy(a)
print(subject, a, b, c, d, e)

subject[1][1] = 'x'

print(subject, a, b, c, d, e)
