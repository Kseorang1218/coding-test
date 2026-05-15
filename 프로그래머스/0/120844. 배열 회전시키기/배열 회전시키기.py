def solution(numbers, direction):
    answer = []
    if direction == "right":
        answer += [numbers.pop(len(numbers)-1)] + numbers
    else:
        tmp = numbers.pop(0)
        answer += numbers + [tmp]
    return answer