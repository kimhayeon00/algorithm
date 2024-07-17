class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        pre = s[0]
        answer = 0
        i = 1
        while i < len(s):
            if dic[pre] >= dic[s[i]]:
                answer += dic[pre]
            else:
                answer -= dic[pre]
            pre = s[i]
            i += 1
        
        answer += dic[s[i-1]]
        return answer
                
