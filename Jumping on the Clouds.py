#!/bin/python

import sys


n = int(raw_input().strip())
c = map(int,raw_input().strip().split(' '))
i = 0
a = 0
while i<n-1:
    if (i+2)>=n:
        a += 1
        break
    elif c[i+2]==1:
        i += 1
        a += 1
    elif c[i+2]!=1:
        i += 2
        a += 1

        
print a
        
