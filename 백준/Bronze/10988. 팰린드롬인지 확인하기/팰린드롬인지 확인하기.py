a = list(input())
b = len(a)//2
c = 0
for i in range(b) :
    if a[i] == a[-i-1] :
        c += 1
    else :
        pass
if c == b :
    print(1)
else :
    print(0)