s= input()
out = 0

for n in s:
    if out <= 1 or int(n) <=1:
        out += int(n)
    else:
        out *= int(n)
print(out)

################################################
data = input()
res = int(data[0])

for i in range(1, len(data)):
    num = int(data[i])
    if num <=1 or res <= 1:
        res += num
    else:
        res *= num

print(res)