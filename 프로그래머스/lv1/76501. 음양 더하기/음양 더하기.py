def solution(absolutes, signs):
    list1= []
    list2=[]
    for j in signs:
        if j == True:            
            list1.append(1)
        else:
            list1.append(-1)         
    for i in range(len(signs)): 
        list2.append(absolutes[i]* list1[i])
    return sum(list2)
        
        
        
                

