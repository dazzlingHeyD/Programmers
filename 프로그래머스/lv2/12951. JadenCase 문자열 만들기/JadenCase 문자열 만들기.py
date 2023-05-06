# def solution(s):
#     list = s.split()
#     new_=[]
#     for i in list:
#         new_.append(i.capitalize())
        
#     return " ".join(new_)
def solution(s):
    s_s = s.split(' ')
    temp = []
    for i in s_s:
        i = i.capitalize()
        temp.append(i)
    return ' '.join(temp)
