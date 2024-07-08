class Solution {
    func findTheWinner(_ n: Int, _ k: Int) -> Int {
        var start = 0
        var lst : [Int] = []
        var idx : Int
        for i in 1...n{
            lst.append(i)
        }

        while lst.count > 1 {
            idx = (start + k - 1) % lst.count
            lst.remove(at:idx)
            start = idx
        }
        return lst[0]
    }
}
