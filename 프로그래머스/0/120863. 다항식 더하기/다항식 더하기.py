def solution(polynomial):
    numberlist = polynomial.split()
    x,s = 0,0
    for i in numberlist :
        if i[-1] == "x" :
            if i[:-1] : x += int(i[:-1])
            else : x += 1
        elif i.isdigit() : s += int(i)
        
    if x == 1 :
        if s > 0 : return f"x + {s}"
        else : return f"x"
    elif x > 1 :
        if s > 0 : return f"{x}x + {s}"
        else : return f"{x}x"
    else : return f"{s}"