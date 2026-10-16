class Solution(object):
    def findDifference(self, nums1, nums2):
        s1=set(nums1)
        s2=set(nums2)
        ans=[]
        ans.append(list(s1-s2))
        ans.append(list(s2-s1))
        return ans