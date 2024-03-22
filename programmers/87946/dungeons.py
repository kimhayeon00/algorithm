from itertools import permutations

def solution(k, dungeons):
    answer = -1
    mx = 0
    lst = list(permutations(dungeons))
    for i in range(len(lst)):
        np = k
        tmp = 0
        for j in range(len(lst[0])):
            if lst[i][j][0] <= np:
                np -= lst[i][j][1]
                tmp += 1
        mx = max(tmp, mx)
            
    return mx
