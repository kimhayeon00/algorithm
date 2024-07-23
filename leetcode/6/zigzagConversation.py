class Solution:
    def convert(self, s: str, numRows: int) -> str:
        mtx = [[]for i in range(numRows)]
        if numRows == 1:
            return s
        for i in range(len(s)):
            tmp = i % (numRows * 2 - 2) 
            if tmp == 0:
                mtx[0].append(s[i])
            elif tmp == numRows-1:
                mtx[-1].append(s[i])
            else:
                if tmp >= numRows:
                    mtx[numRows - tmp + numRows - 2].append(s[i])
                else:
                    mtx[tmp].append(s[i])
        answer = ""
        for i in mtx:
            for j in i:
                answer += j
        return answer
        
