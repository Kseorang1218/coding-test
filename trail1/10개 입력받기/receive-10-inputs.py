lst = list(map(int, input().split()))
n = len(lst)
idx = 0
tot = 0
if 0 in lst:
    for i in range(n):
        if lst[i] == 0:
            idx = i
    for i in range(idx, -1, -1):
            tot += lst[i]
    print(tot, round(tot/idx, 1))
else:
    tot = sum(lst)
    print(tot, round(tot/n, 1))