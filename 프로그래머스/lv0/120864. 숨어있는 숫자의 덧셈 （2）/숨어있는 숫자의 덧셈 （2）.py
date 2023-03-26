import re
def solution(my_string):
    answer = 0
    answer = 0
    result = re.findall(r'\d+', my_string)
    result = list(map(int, result))
    for i in range(len(result)) :
        answer += result[i]
    return answer