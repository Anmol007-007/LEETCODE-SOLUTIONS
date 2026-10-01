class Solution:
    def rob(self, nums: list[int]) -> int:
        prev=maxi=0
        for i in nums:
            rob=max(maxi,prev+i)
            prev=maxi
            maxi=rob
        return maxi