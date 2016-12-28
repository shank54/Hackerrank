#https://www.hackerrank.com/challenges/kangaroo
#!/bin/python3

import sys


x1,v1,x2,v2 = input().strip().split(' ')
x1,v1,x2,v2 = [int(x1),int(v1),int(x2),int(v2)]
#x1+nv1 = x2+nv2
#n(v1-v2) = x2-x1
n=0
if v1!=v2:
    n=(x2-x1)%(v1-v2)
if n==0 and v1>v2:
    print("YES")
else:
    print("NO")
    
    
    
