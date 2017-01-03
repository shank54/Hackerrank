s = str(raw_input())
c = 0
for x in range(len(s)):
    if ord(str(s[x]))>=65 and ord(str(s[x]))<=90:
        c += 1
print c+1