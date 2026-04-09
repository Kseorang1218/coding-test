def solution(n, lost, reserve):
    remain=[]
    
    reserve.sort()  # 정렬 추가
    
    # 겹치는 학생 먼저 처리 (복사본 순회)
    for i in reserve[:]:
        if i in lost:
            lost.remove(i)
            reserve.remove(i)
            remain.append(i)
    
    for i in range(n):
        if i+1 not in lost and i+1 not in reserve and i+1 not in remain:
            remain.append(i+1)
    
    for i in reserve[:]:  # 복사본 순회
        left = i-1
        right = i+1
        if left in lost:
            lost.remove(left)
            remain.append(left)
        elif right in lost:
            lost.remove(right)
            remain.append(right)
    
    new = reserve+remain
    answer = len(new)
    return answer