lst=list(map(int, input().split()))
for i in range(len(lst)):
    if lst[i] == 0:
        print(lst[i-1]+lst[i-2]+lst[i-3])
        break