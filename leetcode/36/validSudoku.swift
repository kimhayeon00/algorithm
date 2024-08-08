class Solution {
    func isValidSudoku(_ board: [[Character]]) -> Bool {
        // 행, 열, 및 박스를 추적하는 Set을 생성
        var rows = Array(repeating: Set<Character>(), count: 9)
        var columns = Array(repeating: Set<Character>(), count: 9)
        var boxes = Array(repeating: Set<Character>(), count: 9)
        
        for i in 0..<9 {
            for j in 0..<9 {
                let char = board[i][j]
                if char == "." {
                    continue
                }
                // 행 중복 체크
                if rows[i].contains(char) {
                    return false
                }
                // 열 중복 체크
                if columns[j].contains(char) {
                    return false
                }
                // 박스 중복 체크
                let boxIndex = (i / 3) * 3 + j / 3
                if boxes[boxIndex].contains(char) {
                    return false
                }
                // 현재 문자 추가
                rows[i].insert(char)
                columns[j].insert(char)
                boxes[boxIndex].insert(char)
            }
        }
        
        return true
    }
}
