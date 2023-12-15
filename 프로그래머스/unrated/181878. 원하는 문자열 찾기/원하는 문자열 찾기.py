def solution(myString, pat):
    m,p = myString.lower(),pat.lower()
    if p in m :
        return 1
    else :
        return 0