class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        l,r=0,len(nums)
        m=(l+r)//2
        return nums[m]