lst = list(map(int, input().split()))
idx = len(lst)-1
if 0 in lst:
    for i in range(len(lst)):
        if lst[i]==0:
            idx = i-1
            break
    for i in range(idx, -1, -1):
        print(lst[i], end=' ')
else:
    for i in range(len(lst)-1, -1, -1):
        print(lst[i], end=' ')