#!/bin/python

import sys

def twoStrings(s1, s2):
    d = dict()
    for i in s1:
        d.setdefault(i,0)
        d[i] += 1
    for i in s2:
        if i in d:
            return "YES"
    return "NO"

q = int(raw_input().strip())
for a0 in xrange(q):
    s1 = raw_input().strip()
    s2 = raw_input().strip()
    result = twoStrings(s1, s2)
    print(result)

