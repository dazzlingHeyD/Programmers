def solution(s):
    cnt_p=0
    cnt_y=0
     
    a = s.upper()
    list_a = list(a)
    for i in list_a:
        if i=='P':
            cnt_p +=1
        if i=="Y":
            cnt_y+=1
    
    if cnt_y == cnt_p:
        return True
    elif cnt_y==0 and cnt_p==0:
        return False
    else: 
        return False
    



    