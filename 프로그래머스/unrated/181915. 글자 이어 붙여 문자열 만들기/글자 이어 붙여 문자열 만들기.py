def solution(my_string, index_list):
    answer = []
    my_string = list(my_string)
    for i in index_list : 
        answer.append(my_string[i])
    return (''.join(str(s) for s in answer))