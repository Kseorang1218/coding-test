# 2차원 배열 선언 및 출력

row, col = 5, 3
grid = [[0] * col for _ in range(row)]

for i in range(row):
    for j in range(col):
        print(grid[i][j])

print("\n행렬 형태로 출력하기:")

for i in range(row):
    for j in range(col):
        print(grid[i][j], end='')
    print()
