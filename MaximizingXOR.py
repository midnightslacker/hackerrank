#!/bin/python

# Complete the function below.
def  maxXor( l,  r):
    result = 0
    for i in range(l,r+1):
        for j in range(l,r+1):
            temp = i ^ j
            if temp > result:
                result = temp
    return result
            
_l = int(raw_input());

_r = int(raw_input());

res = maxXor(_l, _r);
print(res)

