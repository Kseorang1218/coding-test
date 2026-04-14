t = int(input())

for _ in range(t):
    n, s = input().split()
    n = int(n)
    s = [i*n for i in s]
    print(''.join(s))