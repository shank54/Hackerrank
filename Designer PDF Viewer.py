d = dict()
a = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
b = map(int, raw_input().split(" "))
s = str(raw_input())
c=1
m = 0
for i in range(len(a)):
    d[a[i]] = b[i]
for i in range(len(s)):
    c = d[s[i]]
    if c>m:
        m =c
print m*len(s)