# 하루는 약 86,400 -> 단순히 1씩 증가시키면서 확인해도 가능!

n = int(input())
cnt = 0

# for i in range(n+1):
#     for j in range(60):
#         for k in range(60):
#             if '3' in str(k) or '3' in str(j) or '3' in str(i):
#                 cnt += 1

# better
for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(k)+str(j)+str(i):
                cnt += 1

print(cnt)