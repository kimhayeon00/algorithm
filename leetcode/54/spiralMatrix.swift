class Solution {
    func spiralOrder(_ matrix: [[Int]]) -> [Int] {
        let m = matrix.count
        let n = matrix[0].count
        var visited = Array(repeating:Array(repeating:false, count:n), count: m)
        let dr = [0, 1, 0, -1]
        let dc = [1, 0, -1, 0]
        var d = 0
        var r = 0
        var c = 0
        var tmp = 0
        var answer = [matrix[0][0]]
        visited[0][0] = true

        while tmp < 2{
            // print(visited, r, c, d)
            let rr = r + dr[d]
            let cc = c + dc[d]
            if rr >= 0 && rr < m && cc >= 0 && cc < n && !visited[rr][cc] {
                r = rr
                c = cc
                visited[r][c] = true
                answer.append(matrix[r][c])
                tmp = 0
            }
            else{
                d = (d+1)%4
                tmp += 1
            }
        }
        return answer
    }
}
