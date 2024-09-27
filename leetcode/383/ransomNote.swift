class Solution {
    func canConstruct(_ ransomNote: String, _ magazine: String) -> Bool {
        var mag = Array(magazine)
        for i in Array(ransomNote){
            if mag.contains(i){
                if let num = mag.firstIndex(of: i){
                    mag.remove(at: num)
                }
            }
            else{
                return false
            }
        }
        return true
    }
}
