N = int(input())
lst = []
for i in range(N):
    lst.append(list(map(int, input().split())))
cnt = 0
for i in range(N):
    lst_tmp = lst[i]
    if sum(lst_tmp)/4 >= 60:
        print("pass")
        cnt += 1
    else:
        print("fail")
print(cnt)
