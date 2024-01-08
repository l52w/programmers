def solution(myStr):
    import re

    answer = re.sub("[a-c]", " ", myStr).split()
    return answer if len(answer) > 0 else ["EMPTY"]