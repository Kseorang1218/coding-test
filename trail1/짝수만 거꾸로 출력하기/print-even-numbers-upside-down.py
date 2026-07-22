N = int(input())
lst = list(map(int, input().split()))
lst_even = []

for i in range(N):
    if lst[i] % 2 == 0:
        lst_even.append(lst[i])
for i in range(len(lst_even)-1, -1, -1):
    print(lst_even[i], end=' ')