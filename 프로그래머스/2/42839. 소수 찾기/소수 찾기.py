from itertools import permutations

def solution(numbers):
    num_list = list(numbers)  # 문자 그대로 다루는 게 편함
    
    candidates = set()
    for length in range(1, len(num_list) + 1):        # ← 모든 길이
        for p in permutations(num_list, length):
            candidates.add(int(''.join(p)))            # ← 문자열 합쳐서 변환
    
    count = 0
    for n in candidates:
        if n < 2:
            continue
        is_prime = True                                # ← 매번 초기화
        for j in range(2, int(n**0.5) + 1):
            if n % j == 0:
                is_prime = False
                break
        if is_prime:
            count += 1
    
    return count