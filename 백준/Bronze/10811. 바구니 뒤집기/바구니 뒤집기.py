n, m = map(int, input().split())
lst = [i+1 for i in range(n)]

for i in range(m):
    i, j = map(int, input().split())
    mid = (i+j)//2
    while i <= mid:
        lst[i-1], lst[j-1] = lst[j-1], lst[i-1]
        i += 1
        j -= 1
for n in lst:
    print(n, end = ' ')
    