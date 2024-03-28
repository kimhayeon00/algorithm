class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        start = 0
        end = 0
        freq = defaultdict(list)
        window = 0

        while end < len(nums):

            if freq[nums[end]]:
                freq[nums[end]] += 1
            else:
                freq[nums[end]] = 1
            if max(freq.values()) > k :
                    freq[nums[start]] -= 1
                    start += 1
            if  max(freq.values()) <= k:
                window = max(end - start+1, window)
            end += 1

        return window

## Time limit
