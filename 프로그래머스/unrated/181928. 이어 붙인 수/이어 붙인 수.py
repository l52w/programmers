def solution(num_list):
    answer = 0
    a,b = [],[]
    for i in range(len(num_list)) :
        if num_list[i]%2 == 0 :
            a.insert(i,num_list[i])
        else :
            b.insert(i,num_list[i])
    a = ''.join(str(s) for s in a)
    b = ''.join(str(s) for s in b)
    a,b = int(a),int(b)
    return a+b