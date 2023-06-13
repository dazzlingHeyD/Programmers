def solution(s):
    answer = 0
    a = ['zero', 'one', 'two', 'three', 'four',
         'five', 'six', 'seven', 'eight', 'nine']
    
    for i in a:
        s = s.replace(i, str(a.index(i)))
        print("s",s)
        print("a.index(i)",a.index(i))
    return int(s)