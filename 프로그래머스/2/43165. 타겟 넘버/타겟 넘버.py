def solution(numbers, target):
    def dfs(idx, val):
        if idx == len(numbers):
            if val == target:
                return 1
            else:
                return 0
        return dfs(idx+1, val+numbers[idx])+dfs(idx+1, val-numbers[idx])
    
    answer = dfs(0, 0)
    
    return answer