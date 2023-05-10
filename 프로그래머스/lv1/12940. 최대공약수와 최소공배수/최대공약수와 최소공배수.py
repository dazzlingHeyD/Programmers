import math


def solution(n, m):
    a = math.gcd(n,m)
    print(a)
    b= (n*m)//a
    return [a,b]