def solution(quiz):
    answer = []
    for i in range(len(quiz)) :
        a,b,c,d,e = quiz[i].split(' ')
        a,c,e = (int(a),int(c),int(e))
        if b == '+' :
            n = a+c
        elif b == '-' :
            n = a-c
        if n == e :
            answer.insert(i,'O')
        else :
            answer.insert(i,'X')
    return answer