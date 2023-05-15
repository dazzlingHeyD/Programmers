

def solution(n):
    cnt = 0
    
    for i in range(1, n+1):
        hap = 0
        for j in range(i, n+1):
            hap += j
            if hap == n:
                cnt += 1
            elif hap > n:
                break
                
    return cnt

            
        
            
            
        
            