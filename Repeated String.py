#!/bin/python

import sys


s = raw_input().strip()
n = long(raw_input().strip())
l = len(s)
a = n%l
b = n/l
x = s.count('a')*b
y = s[:a].count('a')
print x+y

