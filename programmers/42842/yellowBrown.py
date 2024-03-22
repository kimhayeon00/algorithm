def solution(brown, yellow):
    answer = []
    lst = []
    for i in range(yellow+1):
        if i != 0 and yellow%i == 0:
            lst.append([i, yellow//i])
    
    for i in range(len(lst)):
        if lst[i][0]*2 + lst[i][1]*2 + 4 == brown:
            return [lst[i][1]+2, lst[i][0]+2]
        
    return answer
