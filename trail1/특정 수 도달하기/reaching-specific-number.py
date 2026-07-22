a = list(map(int, input().split()))

tot = 0
n = 0
for num in a:
    if num < 250:
        tot += num
        n += 1
    else:
        break
print(tot, round(tot/n, 1))
# print(round(0.222, 2))