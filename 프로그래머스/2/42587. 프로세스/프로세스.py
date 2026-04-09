from collections import deque

def solution(priorities, location):
    answer = 0
    excution = 0

    priority_queue = deque()
    for p in priorities:
        priority_queue.append(p)
        
    maximum_p = max(priority_queue)
    
    while True:
        curr_p = priority_queue.popleft()
        if (curr_p == maximum_p) and (location == 0):
            excution += 1
            break
        location -= 1
        if location < 0:
            priority_queue.append(curr_p)
            location = len(priority_queue)-1
            continue
        if curr_p == maximum_p:
            excution += 1
            maximum_p = max(priority_queue)   
        else:
            priority_queue.append(curr_p)
            
    answer = excution
    return answer