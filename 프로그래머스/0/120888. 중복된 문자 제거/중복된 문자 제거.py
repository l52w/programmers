def solution(my_string):
    answer = []
    for i in range(len(my_string)):
        if my_string[i] in answer :
            pass
        else :
            answer.append(my_string[i])
    return ''.join(answer)