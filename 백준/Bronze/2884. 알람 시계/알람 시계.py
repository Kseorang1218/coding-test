H, M = map(int, input().split())

tot = H * 60 + M
early = 45

t = tot - early

h = t // 60
m = t - h*60
if h < 0:
    h = 24 + h

print(h, m)