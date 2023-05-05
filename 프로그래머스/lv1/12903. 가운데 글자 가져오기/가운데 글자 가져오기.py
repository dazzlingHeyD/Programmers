def solution(s):
    lens = len(s)
    if lens%2==0:        
        return s[int(lens/2)-1:int(lens/2)+1]
    else:
        return s[int(lens//2)]
