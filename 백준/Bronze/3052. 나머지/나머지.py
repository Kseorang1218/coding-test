lst = []
for i in range(10):
    lst.append(int(input()))
    
lst = [i%42 for i in lst]
lst_set = set(lst)
print(len(lst_set))