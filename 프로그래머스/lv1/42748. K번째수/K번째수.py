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

        


