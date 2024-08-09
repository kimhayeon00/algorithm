class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        visited = [[False for _ in range(n)] for _ in range(m)] # 방문 여부 확인
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        d = 0 # 방향 설정
        x = 0
        y = 0
        tmp = 0
        visited[0][0] = True

        answer = [matrix[0][0]]

        while tmp < 2:
            xx = x+dx[d]
            yy = y+dy[d]
            if 0 <= xx < n and 0 <= yy < m and visited[yy][xx] == False:
                x = xx
                y = yy
                visited[y][x] = True
                answer.append(matrix[y][x])
                tmp = 0
            else:
                d = (d+1)%4 # 진행 방향이 방문된 곳이면 방향 변경
                tmp += 1
            

        # print(visited)
        return answer
