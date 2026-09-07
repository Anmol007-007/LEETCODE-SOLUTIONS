class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = [[]]
        
        for num in nums:
            new_subsets = []
            for curr in output:
                new_subsets.append(curr + [num])
            output += new_subsets
            
        return output