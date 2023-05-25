def solution(elements):

    cnt = 0
    numberSet = set()
    
    element_len = len(elements)
    elements = elements * 2
    
    for i in range(element_len) : 
        for j in range(element_len) : 
            numberSet.add(sum(elements[j:j+i+1]))
    cnt = len(numberSet)
    return cnt
                    
                  
