def solution(name, yearning, photo):
    answer = []
    dicts = {na:year for na,year in zip(name,yearning)}
    ans = 0
    for pho in photo:
        for p in pho:
            if p in dicts.keys():
                ans += dicts[p]
        answer.append(ans)
        ans = 0
    return answer