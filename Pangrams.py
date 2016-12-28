n = input().strip()
n = n.replace(" ","")
n=[x.lower() for x in n]
a = list(set(n))
b = len(a)
if b==26:
    print("pangram")
else:
    print("not pangram")