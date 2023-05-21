def solution(num):
    if num==1:
        return 0
    cnt=0
    while True:
        num = num/2 if num % 2 == 0 else (num*3)+1
        cnt+=1
        if num ==1:
            return cnt
        elif cnt==500:
            return -1
    