def solution(my_string):
    answer = []
    my_string = my_string.replace('"','')
    my_string = list(my_string)
    for i in range(len(my_string)) :
        if my_string[i] in answer :
            pass
        else :
            answer.append(my_string[i])
    return ''.join(map(str,answer))