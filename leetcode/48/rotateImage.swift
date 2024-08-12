class Solution {
    func rotate(_ matrix: inout [[Int]]) {
        let tmp = matrix
        let n = matrix.count

        for i in 0..<n{
            for j in 0..<n{
                matrix[i][j] = tmp[n-j-1][i]
            }
        }
    }
} 
