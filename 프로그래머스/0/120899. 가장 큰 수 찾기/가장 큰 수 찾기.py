def solution(array):
    array_2 = sorted(array)
    answer = [array_2[-1], array.index(array_2[-1])]
    return answer