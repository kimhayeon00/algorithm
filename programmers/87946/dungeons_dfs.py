def solution(k, dungeons):
    answer = -1
    visited = [0 for i in range(len(dungeons))]
    result = []
    def dfs(start, tmp):
        if len(tmp) == len(dungeons):
            result.append(tmp[:])
            return
        for i in range(len(dungeons)):
            if visited[i] == 0:
                tmp.append(i)
                visited[i] = 1
                dfs(i, tmp)
                tmp.pop()
                visited[i] = 0
    
    for i in range(len(dungeons)):
        visited[i] = 1
        dfs(i, [i])
        visited[i] = 0
        
    def find(np, lst):
        tmp = 0
        for i in lst:
            if dungeons[i][0] <= np:
                np -= dungeons[i][1]
                tmp += 1
                
        return tmp
            
    for i in range(len(result)):
        answer = max(answer, find(k, result[i]))
            
    return answer
