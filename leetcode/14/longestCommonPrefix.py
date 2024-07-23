class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer = ""
        strs.sort()
        first = strs[0]
        last = strs[-1]
        if first == last:
            return first
            
        for i in range(len(first)):
            if first[i] == last[i]:
                answer += first[i]
            else:
                return answer

        return answer
