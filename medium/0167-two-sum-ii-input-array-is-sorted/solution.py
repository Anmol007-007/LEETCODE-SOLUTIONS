class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        ans=[]
        l,r=0,len(numbers)-1
        while l<r:
            s=numbers[l]+numbers[r]
            if s==target:
                return [l+1,r+1]
            elif s>target:
                r-=1
            else:
                l+=1
        return [-1,-1]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna