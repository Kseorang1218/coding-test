N = int(input())
score = list(map(float, input().split()))
print(round(sum(score)/N, 1))
if sum(score)/N >= 4:
    print("Perfect")
elif sum(score)/N >= 3:
    print("Good")
else:
    print("Poor")