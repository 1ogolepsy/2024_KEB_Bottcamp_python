sugang = dict(python='kim', cpp = 'sung', db='kang')
# print(sugang)
#
# sugang['datastructer']='kim'
# print(sugang)
#
# sugang['datastructer']='park'
# print(sugang)
# print(sugang['db'])
# print(sugang.get('opensource'))
# print(sugang.get('opensource', 'not exist'))
#
# for s in sugang.items():
#     print(s)

for k in sugang.keys():
    print(k)

for v in sugang.values():
    print(v)

print(sugang.keys())
print(type(sugang.keys()))