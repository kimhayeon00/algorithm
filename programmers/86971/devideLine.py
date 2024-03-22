from collections import deque
def solution(n, wires):
    answer = n
    graph = [[] for i in range(n+1)]
    
    # 그래프 만들기
    for i, j in wires:
        graph[i].append(j)
        graph[j].append(i)

    def bfs(start):
        visited = [0 for i in range(n+1)]
        cnt = 1
        que = deque([start])
        visited[start] = 1
        
        while que:
            tmp = que.popleft()
            for i in graph[tmp]:
                if visited[i] == 0:
                    que.append(i)
                    cnt += 1
                    visited[i] = 1
                
        return cnt
    
    # 전선 하나씩 끊어서 비교하기
    for i, j in wires:
        graph[i].remove(j)
        graph[j].remove(i)
        
        answer = min(answer, abs(bfs(i)-bfs(j)))
        
        # 끊은거 다시 추가
        graph[j].append(i)
        graph[i].append(j)
    
    return answer
