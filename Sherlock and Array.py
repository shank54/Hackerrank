m = int(raw_input())
for i in range(m):
    n = int(raw_input())
    l = map(int,raw_input().split())
    a = list()
    b = list()
    a.append(0)
    s = 0
    for j in range(1,len(l)):
        s += l[j-1]
        a.append(s)
    x = len(l)-1
    b.append(0)
    s = 0
    while(x>0):
        s += l[x]
        x -= 1
        b.append(s)
    c = b[::-1]
    y = 0
    for j in range(len(a)):
        if a[j]==c[j]:
            y = 1
            break
    if y==1:
        print "YES"
    else:
        print "NO"