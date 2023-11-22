def solution(my_string, overwrite_string, s):
    a = s + len(overwrite_string)
    return my_string[:s]+overwrite_string[0:]+my_string[a:]
