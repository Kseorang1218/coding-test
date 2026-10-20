n, k = map(int, input().split())

# n=17
# k=4

# n=25
# k=5

## 1
cnt = 0

while n!=1:
    if n%k:
        n = n -1
        cnt +=1
    else:
        n = n//k
        cnt += 1
print(cnt)

# n을 나누는 작업을 많이 하는게 빠르게 줄일 수 있다!
## 2
## n, k가 커져도 로그시간복잡도로 더 빠르게 할 수 있다

cnt = 0
while True:
    target = (n//k)*k
    cnt += (n-target)
    n = target
    if n<k:
        break
    n=n//k
    cnt += 1
cnt += (n-1)
print(cnt)