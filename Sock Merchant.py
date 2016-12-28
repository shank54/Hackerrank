#!/bin/python3

import sys


n = int(input().strip())
c = [int(c_temp) for c_temp in input().strip().split(' ')]
a = []
p=0
for i in range(n):
    if c[i] not in a:
        a.append(c[i])
    else:
        p+=1
        a.remove(c[i])
print(p)        


