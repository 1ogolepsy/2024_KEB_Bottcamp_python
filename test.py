import copy
import random

def change(keep):
    keep =False
    return keep

keep =True
i = 0
while keep:
    if i ==5:
        change(keep)
        print('keep')
    else:
        print(i)
        if i == 10:
            break
    i += 1