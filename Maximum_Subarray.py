class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum=0
        max_sum=nums[0]
        for i in range(0,len(nums)):
            if sum>=0:
                sum=sum+nums[i]
            else:
                sum=nums[i]
            if max_sum< sum:
                max_sum=sum
        return max_sum
