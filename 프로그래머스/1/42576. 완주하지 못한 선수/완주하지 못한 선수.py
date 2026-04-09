from collections import Counter

def solution(participant, completion):
    answer = ''

    p_counter = Counter(participant)
    c_counter = Counter(completion)

    last = dict(p_counter - c_counter)
    for key in last.keys():
        answer = key
        
    return answer