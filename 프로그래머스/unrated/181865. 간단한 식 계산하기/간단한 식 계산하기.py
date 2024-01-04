def solution(binomial):
    answer = 0
    a = ''.join(binomial).split()
    if a[1] == '+' :
        answer = int(a[0])+int(a[2])
    elif a[1] == '-' :
        answer = int(a[0])-int(a[2])
    elif a[1] == '*' :
        answer = int(a[0]) * int(a[2])
    else : 
        answer = int(a[0]) / int(a[2])
    return answer