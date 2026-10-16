class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        ans=[]
        sub1=set()
        sub2=set()
        for i in nums1:
            if i not in nums2:
                sub1.add(i)
        for j in nums2:
            if j not in nums1:
                sub2.add(j)
        ans.append(list(sub1))
        ans.append(list(sub2))
        return ans