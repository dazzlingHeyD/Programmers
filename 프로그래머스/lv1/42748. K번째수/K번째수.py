def solution(array, commands):

    newlist = []
    for i in range(len(commands)):
        a = commands[i][0]
        b = commands[i][1]
        c = commands[i][2]
        list1 = array[a-1:b]
        list1.sort()
        # a= list1[c-1]
        newlist.append(list1[c-1])
        
    return newlist





2
3# 다른 사람 풀이 
# def solution(array, commands):
#     return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))

        


