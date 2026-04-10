from collections import Counter

def solution(nums):
    counter = Counter(nums)
    type_num = len(counter.keys())
    can_get = len(nums)//2
    if type_num <= can_get:
        answer = type_num
    else:
        answer = can_get
    return answer