import math

n = int(input())

grades = list(map(int, input().split()))
max_grade = max(grades)
 
new_grades = [n/max_grade*100 for n in grades]
print(sum(new_grades)/len(new_grades))