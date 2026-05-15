def solution(num, k):
    num = str(num)
    answer = num.find(str(k))
    if answer>=0: answer +=1 
    return answer