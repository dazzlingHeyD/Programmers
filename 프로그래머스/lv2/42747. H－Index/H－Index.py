       
def solution(citations):
    citations.sort()
    print('len(citations):', len(citations))
    print(citations)
    for idx , citation in enumerate(citations):
        print(idx, citation)
        if citation >= len(citations) - idx : # 0>5-0 1>5-1 3>5-3s
            return len(citations) - idx
    return 0
        
