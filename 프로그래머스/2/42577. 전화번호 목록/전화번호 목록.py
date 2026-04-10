def solution(phone_book):
    phone_book=sorted(phone_book)
    answer = True 
    flag=True
    while (answer and flag):
        for i in range(len(phone_book)-1):
            prefix = phone_book[i]
            nexts=phone_book[i+1][:len(prefix)]
            if prefix == nexts:
                    answer = False
        flag = False
        
    return answer