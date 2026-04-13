n, m = map(int, input().split())
ball_list = [0]*n

for _ in range(m):
    tmp = list(map(int, input().split()))
    start = tmp[0]
    end = tmp[1]
    num = tmp[2]
    for i in range(start, end+1):
        ball_list[i-1] = num
    if start==end:
        ball_list[start-1] = num

for n in ball_list:
    print(n, end=' ')
