class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l, r = 0, k
        n = len(nums)
        
        curr_sum = sum(nums[:k])
        max_sum = curr_sum
        while r < n:
            curr_sum += nums[r] - nums[l]
            max_sum = max(max_sum, curr_sum)
            l += 1
            r += 1
            
        return max_sum / k