class Solution:
    def jump(self, nums: List[int]) -> int:
        l,r=0,0
        jump=0
        n=len(nums)
        while r<n-1:
            reach=0
            for i in range(l,r+1):
                reach = max(i+nums[i],reach)
            l=r+1
            r=reach
            jump+=1
        return jump