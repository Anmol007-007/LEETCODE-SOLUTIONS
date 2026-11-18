class Solution(object):
    def removeDuplicates(self, nums):
        l,r=0,0
        n=len(nums)
        while r<n:
            if nums[l]==nums[r]:
                r+=1
            else:
                l+=1
                nums[l]=nums[r]
                r+=1
        return l+1
        