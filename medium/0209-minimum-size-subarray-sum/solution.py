class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        l,s,m=0,0,float('inf')
        for i in range(len(nums)):
            s+=nums[i]
            while s>=target:
                m=min(m,i-l+1)
                s-=nums[l]
                l+=1
        return 0 if m==float('inf') else m