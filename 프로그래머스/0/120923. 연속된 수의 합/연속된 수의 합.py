def solution(num, total):
    ans = []
    if num%2 == 0 :
        a = total//num
        ans.append(a)
        ans.append(a+1)
        for i in range(1, num//2) :
            ans.append(a-i)
        for j in range(1, num//2) :
            ans.append(a+1+j)
    else :
        b = total//num
        ans.append(b)
        for i in range(1, num//2+1) :
            ans.append(b-i)
        for j in range(1, num//2+1) :
            ans.append(b+j)
    return sorted(ans)