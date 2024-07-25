class Solution {
    func isPalindrome(_ s: String) -> Bool {
        var tmp = ""

        for i in s{
            if i.isLetter || i.isNumber{
                tmp.append(i.lowercased())
            }
        }
        let pmt = String(tmp.reversed())
        if pmt == tmp{
            return true
        }
        return false
    }
}
