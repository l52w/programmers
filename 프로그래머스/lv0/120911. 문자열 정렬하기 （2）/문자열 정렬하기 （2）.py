def solution(my_string):
    answer = ''
    a = []
    my_string = my_string.lower()
    for i in range(len(my_string)) :
        a.append(my_string[i])
        a.sort()
    answer = ''.join(map(str, a))
    return answer