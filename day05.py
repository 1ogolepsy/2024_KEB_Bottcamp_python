# def out_func(nout):
#     def innner_func(nin):
#         return nin * nin
#     return innner_func((nout))
#
# print(out_func(5))

#closure
def out_func(nout):
    def innner_func():
        return nout * nout
    return innner_func

x = out_func(5)
print(x())