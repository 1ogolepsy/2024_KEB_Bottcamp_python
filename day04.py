t1= (5)
t2 = 5,
t3 = (5,)
t4 = (5, 7)
t5 = 5, 7
print(type(t1), type(t2), type(t3), type(t4), type(t5))
t6 = 'python', 'kim' #packing
print(type(t6), t6[1])
subject, prof = t6 #unpacking
print(subject, prof)
t7 = ()
print(type(t7))
t9 = 1, 2, 3
t10 = 1, 2
print(t9 == t10)
print(t9 < t10)
t11 = 4.43,
t12 = 4.97, 4.1, 3.27
print(t11 + t12)
print(id(t11))
t11 = t11 + t12
print(t11)
print((id(t11)))


