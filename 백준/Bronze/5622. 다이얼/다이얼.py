num_lst = [(2, 'ABC'), (3, 'DEF'), (4, 'GHI'), (5, 'JKL'), (6, 'MNO'), (7, 'PQRS'), (8, 'TUV'), (9, 'WXYZ')]

num_input = input()

tot = 0 
for n in num_input:
    for i in range(len(num_lst)):
        if n in num_lst[i][1]:
            time = num_lst[i][0]+1
            tot+=time
print(tot)
