class Solution {
    func intToRoman(_ num: Int) -> String {
        let dic: [(value: Int, symbol: String)] = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]
        var result = ""
        var num = num
        for item in dic{
            while num >= item.value{
                result += item.symbol
                num -= item.value
            }
        }
        return result
    }
}
