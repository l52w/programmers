def solution(ineq, eq, n, m):
    answer = 0
    if n<m :
        if ineq=="<" and eq=="=" :
            answer = 1
        elif ineq=="<" and eq=="!" :
            answer = 1
        elif ineq==">" and eq=="=" :
            answer = 0
        else :
            answer = 0
    elif n>m :
        if ineq=="<" and eq=="=" :
            answer = 0
        elif ineq=="<" and eq=="!" :
            answer = 0
        elif ineq==">" and eq=="=" :
            answer = 1
        else :
            answer = 1
    else :
        if ineq=="<" and eq=="=" :
            answer = 1
        elif ineq=="<" and eq=="!" :
            answer = 0
        elif ineq==">" and eq=="=" :
            answer = 1
        else :
            answer = 0
    return answer