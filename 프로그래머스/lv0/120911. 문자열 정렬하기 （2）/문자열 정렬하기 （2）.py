def solution(my_string):
    answer = ''
    a = []
    my_string = my_string.lower()
    for i in range(len(my_string)) :
        a.append(my_string[i])
        a.sort()
    answer = ''.join(map(str, a))
    return answer

# 다른 사람의 풀이
# def solution(my_string):
#     return ''.join(sorted(my_string.lower()))
