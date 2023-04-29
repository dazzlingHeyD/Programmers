def solution(seoul):
    
    for i in seoul:
        if i=="Kim":
            a = seoul.index('Kim')
            ans = "김서방은 {}에 있다".format(a)
            return ans
    