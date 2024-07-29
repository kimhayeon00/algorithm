class Solution {
    func twoSum(_ numbers: [Int], _ target: Int) -> [Int] {
        var pre : Int = 0
        var last : Int = Int(numbers.count) - 1

        while pre < last{
            if numbers[pre] + numbers[last] == target{
                return [pre+1, last+1]
            } else if numbers[pre] + numbers[last] < target{
                pre += 1
            } else{
                last = last - 1
            }
        }
        return [pre+1, last+1]
    }
}
