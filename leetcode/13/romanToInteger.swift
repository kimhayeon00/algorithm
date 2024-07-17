class Solution {
    func romanToInt(_ s: String) -> Int {
        var answer  = 0
        let dic : [Character:Int] = ["I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000]
        var pre : Int = 0

        for i in s {
            if let now = dic[i]{
                if now > pre{
                    answer -= pre * 2
                }
                answer += now
                pre = now
            }
        }
        return answer
    }
}
