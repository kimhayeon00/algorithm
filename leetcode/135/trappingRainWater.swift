class Solution {
    func trap(_ height: [Int]) -> Int {
        var n = height.count
        var answer = 0

        if n == 0{
            return 0
        }
        var left : [Int] = [height[0]]
        var right : [Int] = [height[n-1]]

        for i in 1..<n{
            left.append(max(left[i-1], height[i]))
        }

        for i in stride(from: n-2, through: 0, by: -1){
            right.append(max(right[n-i-2], height[i]))
        }

        for i in 0..<n{
            answer += min(left[i], right[n-i-1]) - height[i]
        }
        return answer
    }
}
