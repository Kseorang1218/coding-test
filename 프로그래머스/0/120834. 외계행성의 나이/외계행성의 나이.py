def solution(age):
    answer = ''
    for s in str(age):
        answer += chr(int(s)+97)
    return answer