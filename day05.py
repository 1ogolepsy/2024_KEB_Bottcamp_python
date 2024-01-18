univ ='inha university'
# counts_alphabet = {letter: univ.count(letter) for letter in univ}
# print(counts_alphabet)

counts_alphabet = {}
for i in univ:
    counts_alphabet.update({i:univ.count(i)})
    #counts_alphabet[i] = univ.count(i)

print(counts_alphabet)