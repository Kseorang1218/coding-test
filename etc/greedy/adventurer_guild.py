
## 못풂!!!
data = map(int, input().split())
data.sort()

res=0 # 총 그룹 수
cnt=0 # 현재 그룹에 포함된 모험가 수

for i in data:  # 공포도를 낮은것부터 확인
    cnt += 1    # 현재 그룹에 모험가 포함
    if cnt >= i:    # 현재 그룹에 포함된 모험가가 공포도 이상이면 그룹 결성
        res += 1
        cnt = 0
print(res)