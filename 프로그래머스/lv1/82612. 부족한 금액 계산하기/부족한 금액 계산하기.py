def solution(price, money, count):
    hap=0
    for i in range(1,count+1):
        hap+=i*price
    if hap>money:
        return hap-money
    else: return 0
    
    



    