def solution(n_str):
    a = list(n_str)
    for i in range(len(a)) :
        if a[0] == "0" :
            a.pop(int(a[0]))
    return ''.join(a)