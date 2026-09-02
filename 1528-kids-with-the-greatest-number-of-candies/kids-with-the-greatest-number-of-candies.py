class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result=[]
        curr_max=max(candies)
        for i in candies:
            if i+extraCandies>=curr_max:
                result.append(True)
            else:
                result.append(False)
        return result