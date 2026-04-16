s = input().upper()
s_set = list(set(s))

cnt_lst = []
for i in s_set:
    cnt_lst.append((i, s.count(i)))

cnt_lst_sorted = sorted(cnt_lst, key=lambda x: x[1], reverse=True)

if len(cnt_lst_sorted) > 1 and cnt_lst_sorted[0][1] == cnt_lst_sorted[1][1]:
    print('?')
else:
    print(cnt_lst_sorted[0][0])