class Solution {
    func minOperations(_ logs: [String]) -> Int {
        var answer = 0
        var newname : String
        for name in logs{
            let idx = name.firstIndex(of:"/") ?? name.endIndex
            newname = String(name[..<idx])
            if ".." == newname {
                answer -= 1
                answer = max(answer, 0)
            }
            else if "."  == newname{
                continue
            }
            else{
                answer += 1
            }
        }
        return answer
    }
}
