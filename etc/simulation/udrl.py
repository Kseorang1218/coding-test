# 못풂!!!!!!!!!!!!!!!

# n = int(input())
# plan = input().split()

# x = 0
# y = 0
# for direction in plan:
#     if direction == 'R':
#         ny = y +1
#     elif direction == 'L':
#         ny = y-1
#     elif direction == 'U':
#         nx = x-1
#     else:
#         nx = x+1
#     if nx >= n or nx < 0 or ny >= n or ny < 0:
#         continue
#     x, y = nx, ny

# print(y, x)


### Solution ###
n = int(input())
plan = input().split()

x = 0
y = 0

# L R U D
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
moves = ['L', 'R', 'U', 'D']
for direction in plan:
    for i in range(4):
        if direction == moves[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx >= n or nx < 0 or ny >= n or ny < 0:
        continue
    x, y = nx, ny

print(x+1, y+1)
