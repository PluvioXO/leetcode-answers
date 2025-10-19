class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # We follow 1 rule, if sum is negative start new subarray, if sum is positive extend. 
        i = 0 
        c = float('-inf') 
        t = 0 
        while i != len(nums): 
            t = nums[i] if t < 0 else t+nums[i]
            c = max(c, t)
            i += 1
        return c 
            