def solution(my_string, m, c) :
    import numpy as np
    
    answer = []    
    b = len(my_string) // m
    my_string = list(my_string)
    a = np.array(my_string)
    a = a.reshape(b,m)
    
    for i in range(b) :
        answer.append(a[i][c-1])
    answer = ''.join(str(s) for s in answer)
    return answer