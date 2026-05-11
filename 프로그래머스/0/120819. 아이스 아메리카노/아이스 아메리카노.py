def solution(money):
    import math
    can_drink = math.ceil(money//5500)
    answer = [can_drink, money-can_drink*5500]
    
    return answer