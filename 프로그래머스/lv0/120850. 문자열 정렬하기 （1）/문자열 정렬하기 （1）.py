def solution(my_string):
    answer = []
    my_list = list(my_string)
    for i in range(len(my_list)) :
        if my_list[i].isdigit() :
            my_list[i] = int(my_list[i])
            answer.append(my_list[i]) 
    answer.sort()
    return answer