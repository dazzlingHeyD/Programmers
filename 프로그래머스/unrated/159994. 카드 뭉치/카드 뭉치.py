def solution(cards1, cards2, goal):
    cards1_index , cards2_index = 0,0
    for word in goal:
        if len(cards1) > cards1_index and word == cards1[cards1_index]:
            cards1_index += 1
        elif len(cards2) > cards2_index and word == cards2[cards2_index]:
            cards2_index += 1
        else:
            return "No"
 
    return 'Yes'

    
    




        
        
