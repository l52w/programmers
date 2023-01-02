import re
def solution(my_string):
    a = re.findall(r'\d', my_string)
    b = list(map(int, a))
    return sum(b)