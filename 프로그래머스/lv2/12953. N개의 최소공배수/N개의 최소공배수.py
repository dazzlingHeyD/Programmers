def lcm(a,b):
    for i in range(max(a,b),(a*b)+1):
        if i%a==0 and i%b==0:
            return i 
        
        
def solution(arr):
    a,b = arr[0], arr[1]
    re_lcm = lcm(a,b)
    for i in range(1,len(arr)-1):
        if i ==1:
            a,b = re_lcm, arr[i+1]
            res_lcm = lcm(a,b)
        else: 
            a,b = res_lcm, arr[i+1]
            res_lcm = lcm(a,b)
        
    return res_lcm 


        
        


        
    