t = int(input())
for j in range(t):
    s = str(raw_input())
    c = 0
    for i in range(1,len(s)):
        if s[i-1]==s[i]:
            c += 1
    print c