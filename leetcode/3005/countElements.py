class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        arr1 = sorted(nums)
        arr2 = set(nums)
        result = []
        answer = 0
        
        for i in arr2:
            result.append(arr1.count(i))
        print(result)
        maxR = max(result)
        for i in result:
            if i == maxR:
                answer += i
        return answer
                
