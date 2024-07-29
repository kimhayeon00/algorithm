class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums.sort()

        for i in range(len(nums)):
            pre = 0
            last = len(nums) - 1
            while pre < last:
                if i != pre and i != last:
                    s = nums[i] + nums[pre] + nums[last]
                    if s == 0:
                        answer.append([nums[i], nums[pre], nums[last]])
                        break
                    elif s < 0:
                        pre += 1
                    else:
                        last -= 1
                elif i == pre:
                    pre += 1
                else:
                    last -= 1


        
