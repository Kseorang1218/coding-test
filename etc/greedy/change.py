n = 1260
count=0

coin = [500, 100, 50, 10]

for c in coin:
    count += n//c
    n = n%c

print(count)

# 시간복잡도는? -> O(K)