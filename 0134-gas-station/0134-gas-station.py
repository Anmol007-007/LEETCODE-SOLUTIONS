class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        curr,res=0,0
        if sum(gas)<sum(cost):
            return -1
        for i in range(len(gas)):
            curr+=gas[i]-cost[i]
            if curr<0:
                curr=0
                res=i+1
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna