n = map(int,raw_input().split(" "))
m = map(int,raw_input().split(" "))
c=0
for i in range(0,n[0]):
    for j in range(i+1,n[0]):
        if (m[i]+m[j])%n[1]==0:
            c+=1
print c
