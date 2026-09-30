class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        arr=[0]*len(cost)
        arr[0]=cost[0]
        if len(cost)>=2:
            arr[1]=cost[1]
        for i in range(2,len(cost)):
            arr[i]=cost[i]+min(arr[i-2],arr[i-1])
        return min(arr[-1],arr[-2])