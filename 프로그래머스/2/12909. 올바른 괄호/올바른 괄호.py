from collections import deque

def solution(s):
    answer = True
    queue = deque()
    for i in range(len(s)):
        if s[i] == '(':
            queue.append(s[i])
        elif s[i] == ')':
            if not queue:
                return False
            else:
                queue.popleft()
    if queue:
        return False
    else:
        return True