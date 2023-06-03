def solution(t, p):
    cnt=0
    cp = len(p)
    a = len(t)-len(p)+1 # 비교횟수 
    list1 = []
    for i in range(a):
        list1.append(t[i:i+cp])
    print(list1)
    list2 = []
    for i in list1:
        list2.append(int(i))   
        
    for i in list2:
        if int(p) >= i :
            cnt+=1
    print(cnt)
    return cnt
            
        