class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[1]*n
        pre=1
        next=1
        for i in range(n):
            ans[i]*=pre
            pre*=nums[i]
            ans[~i]*=next
            next*=nums[~i]
        return ans