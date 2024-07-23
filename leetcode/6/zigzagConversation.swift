class Solution {
    func convert(_ s: String, _ numRows: Int) -> String {
        // 기본 조건: numRows가 1일 경우 문자열 그대로 반환
        if numRows == 1 {
            return s
        }

        // 문자열을 저장할 2차원 배열 초기화
        var rows: [String] = Array(repeating: "", count: min(numRows, s.count))
        var currentRow = 0
        var goingDown = false

        // 문자열을 대응되는 행에 추가
        for char in s {
            rows[currentRow] += String(char)
            if currentRow == 0 || currentRow == numRows - 1 {
                goingDown.toggle()
            }
            currentRow += goingDown ? 1 : -1
        }

        // 모든 행을 합쳐 최종 문자열 완성
        return rows.joined()
    }
}
