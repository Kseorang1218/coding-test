# 상하좌우

# n = int(input())
# plans = list(input().split())
n = 5
plans = ['R', 'R', 'R', 'U', 'D', 'D']

x, y = 1, 1

dx = [0, 0, -1, 1]
dy  = [-1, 1, 0, 0]
move = ['L', 'R', 'U', 'D']

for plan in plans:
  for i in range(len(move)):
    if plan == move[i]:
      nx = x + dx[i]
      ny = y + dy[i]
  if nx < 1 or nx > n or ny < 1 or ny > n:
    continue
  x, y = nx, ny

# or

for plan in plans:
  idx = move.index(plan)
  nx = x + dx[idx]
  ny = y + dy[idx]
  if nx < 1 or nx > n or ny < 1 or ny > n:
    continue
  x, y = nx, ny
  
print(x, y)