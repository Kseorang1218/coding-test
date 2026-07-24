lst = list(map(int, input().split()))

even = lst[1]+lst[3]+lst[5]+lst[7]+lst[9]
odd = lst[0]+lst[2]+lst[4]+lst[6]+lst[8]

print(abs(even-odd))