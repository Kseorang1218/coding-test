import math
def solution(n):
    # print( math.gcd(n, 6))
    answer = ((n*6) // math.gcd(n, 6))//6
    return answer