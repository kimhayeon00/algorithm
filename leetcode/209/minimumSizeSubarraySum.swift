class Solution {
    func minSubArrayLen(_ target: Int, _ nums: [Int]) -> Int {
        var minCount = nums.count + 1
        var sum = 0
        var left = 0

        for (right, num) in nums.enumerated(){
            sum += num

            while sum >= target{
                sum -= nums[left]
                minCount = min(minCount, right - left + 1)
                left += 1
            }
        }
        return minCount > nums.count ? 0 : minCount
    }
}
