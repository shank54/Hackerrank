n = int(raw_input())
t = [0]*n
d = [0]*n
x = [0]*n
for i in range(n):
    a = map(int,raw_input().split())
    t[i] = a[0]
    d[i] = a[1]
    x[i] = t[i]+d[i]
l = list()
for i in range(len(x)):
    l.append((i+1,x[i]))
l.sort(key=lambda tup: tup[1])
for i in l:
    print i[0],