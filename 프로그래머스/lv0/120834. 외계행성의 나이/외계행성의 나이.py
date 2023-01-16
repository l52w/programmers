import string
def solution(age):
    answer = ''
    a = list(map(int, str(age)))
    b = list(string.ascii_lowercase)
    c = []
    for i in range(len(a)) :
        c.append(b[a[i]])
    answer = ''.join(map(str, c))
    return answer