class Solution:
    def minOperations(self, logs: List[str]) -> int:
        answer = 0
        for name in logs:
            if ".." in name and answer > 0:
                answer -=1
            elif "." in name:
                pass
            else:
                answer += 1
        return answer
