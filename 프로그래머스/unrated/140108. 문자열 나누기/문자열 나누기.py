def solution(s):
    answer = 0
    one=0; not_one=0
    for i in s:
        if one==not_one:
            answer+=1
            k=i
            print(k)
        if k==i:
            one+=1
        else:
            not_one+=1       
    return answer
        
    