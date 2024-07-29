class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        pre = 0
        last = len(numbers)-1

        while pre < last:
            if numbers[pre] + numbers[last] == target:
                return [pre+1, last+1]

            elif numbers[pre] + numbers[last] < target:
                pre += 1
            else:
                last -= 1
        
