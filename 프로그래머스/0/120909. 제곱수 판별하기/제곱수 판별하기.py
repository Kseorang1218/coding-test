def solution(n):
    answer = 0
    if int(n**0.5)*int(n**0.5) == n:
        answer=1
    else:
        answer=2
    return answer