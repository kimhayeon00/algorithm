class Solution {
    func longestCommonPrefix(_ strs: [String]) -> String { 
        let sortedStrs = strs.sorted()
        
        guard let first = sortedStrs.first, let last = sortedStrs.last else {
            return ""
        }

        if first == last{
            return first
        }

        var prefix = first
        while !last.hasPrefix(prefix){
            prefix = String(prefix.dropLast())
        }
        return prefix
    }
}
