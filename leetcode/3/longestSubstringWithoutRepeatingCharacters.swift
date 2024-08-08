class Solution {
    func lengthOfLongestSubstring(_ s: String) -> Int {
        var start = 0
        var maxLength = 0
        var charIndexMap: [Character: Int] = [:]
        let characters = Array(s)
        
        for (i, char) in characters.enumerated() {
            if let index = charIndexMap[char], index >= start {
                start = index + 1
            }
            charIndexMap[char] = i
            print(charIndexMap)
            maxLength = max(maxLength, i - start + 1)
        }
        
        return maxLength
    }
}
