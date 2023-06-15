def solution(n, k):
    list1 = []
    cnt =  n//k
    i=1
    
    for i in range(1,cnt+1):
        list1.append(i*k)
        i+=1    
    return list1