def solution(str_list):
    answer = []
    for i in range(len(str_list)) :
        if "l" in str_list[i] :
            for i in range(0,i) :
                answer.append(str_list[i])
            break
        elif "r" in str_list[i] :
            for i in range(i+1,len(str_list)) :
                answer.append(str_list[i])
            break
        else :
            answer = []
    return answer