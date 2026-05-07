# 446. Arithmetic Slices II - Subsequence
# Given an integer array nums, return the number of all the arithmetic subsequences of nums.

# A sequence of numbers is called arithmetic if it consists of at least three elements 
# and if the difference between any two consecutive elements is the same.

class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        n = len(nums)
        dp = [{} for _ in range(n)]
        res = 0
        
        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                
                # get previous count
                count = dp[j].get(diff, 0)
                
                # add to result (only sequences of length >= 3)
                res += count
                
                # update dp
                dp[i][diff] = dp[i].get(diff, 0) + count + 1
        
        return res