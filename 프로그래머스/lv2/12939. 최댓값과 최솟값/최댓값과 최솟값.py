def solution(s):
    a =  s.split(" ")
    print(a)
    b= list(map(int,a))
    print(b)
    mx = max(b)
    mn = min(b)
    return "{} {}".format(mn,mx)