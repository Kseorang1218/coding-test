row, col = 8, 8

pos = input()
x=ord(pos[0])-ord('a')
y=int(pos[1])-1

# 동서남북
dx=[1, 1, -1, -1]
dy=[1, -1, 1, -1]

cnt = 0
for i in range(4):
    nx = x + 2*dx[i]
    ny = y + dy[i]
    if nx < 0 or nx >= row or ny < 0 or ny >= col:
        continue
    cnt += 1

for i in range(4):
    nx = x + dx[i]
    ny = y + 2*dy[i]
    if nx < 0 or nx >= row or ny < 0 or ny >= col:
        continue
    cnt += 1

print(cnt)

## better
pos = input()
y=ord(pos[0])-ord('a')
x=int(pos[1])-1
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

res = 0
for step in steps:
    nx = x+step[0]
    ny = y+step[1]
    if nx < 0 or nx >= row or ny < 0 or ny >= col:
        continue
    res += 1

print(cnt)