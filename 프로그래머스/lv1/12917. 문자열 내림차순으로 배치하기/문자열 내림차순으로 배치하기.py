def solution(s):
    a = list(s)
    sorted_A = sorted(a,reverse=True)
    print(sorted_A)
    return ''.join(sorted_A)