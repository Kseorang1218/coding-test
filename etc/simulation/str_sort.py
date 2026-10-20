s = input()
s = sorted(s)

res = ""
num = 0

for val in s:
    if val.isalpha():
        res += val
    else:
        num += int(val)

## 엣지 케이스!! (숫자가 없는 경우)
# print(res+str(num))
if num:
    print(res+str(num))
else:
    print(res)