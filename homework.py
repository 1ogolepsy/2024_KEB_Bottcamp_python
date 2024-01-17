e2f = {'dog':'chien','cat':'chat','walrus':'morse'}

#8.6.1
print(e2f)

#8.6.2
print(list(e2f)[2])

#8.6.3
f2e = dict(e2f.items())
print(f2e)

#8.6.4
print(e2f['dog'])

#8.6.5
print(list(e2f.keys()))

#8.6.6
life = dict(animals={'cats':'Henri','octopi':'Grumpy','emus':'Lucy'},plants={},other={})
print(life)

#8.6.7
print(list(life.keys()))

#8.6.8
print(list(life['animals'].keys()))

#8.6.9
print(life['animals']['cats'])

#8.6.10
square = {keys:values for keys, values in zip(range(10),[i*i for i in range(10)])}
print(square)

#번외편, e2f의 key와 value를 반대로 한 f2e를 만든다면
f2e={}
print(list(e2f.items()))

for i in range(len(e2f)):
    new_key = list(e2f.items())[i][1]
    new_value = list(e2f.items())[i][0]
    f2e.update({new_key:new_value})

print(f2e)
