class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0
        left = [height[0]]
        right = [height[-1]]
        for i in range(1, n):
            left.append(max(left[-1],height[i]))
        
        for i in range(n-2, -1, -1):
            right.append(max(right[-1], height[i]))

        answer = 0
        for i in range(n):
            answer += min(left[i], right[n-i-1]) - height[i]

  
        return answer
