def solution(arr, divisor):
    ans=[]
    for i in arr:
        if i%divisor ==0:
            ans.append(i)   
            print(ans)
    if ans ==[]:
        return [-1]
    re = sorted(ans)
    return re