def solution(numbers, target):
    def dfs(idx, tot):
        if idx == len(numbers):
            if tot == target:
                return 1 
            else:
                return 0
        return dfs(idx+1, tot+numbers[idx]) + dfs(idx+1, tot-numbers[idx])
    
    answer = dfs(0,0)
    return answer