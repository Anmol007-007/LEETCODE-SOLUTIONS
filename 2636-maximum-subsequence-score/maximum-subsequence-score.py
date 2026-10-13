class Solution:
    def maxScore(self, nums1: list[int], nums2: list[int], k: int) -> int:
        pair=sorted(zip(nums2,nums1),reverse=True)
        curr,maxi,mheap=0,0,[]
        for n2,n1 in pair:
            heapq.heappush(mheap,n1)
            curr+=n1

            if len(mheap)>k:
                curr-=heapq.heappop(mheap)
            if len(mheap)==k:
                maxi=max(curr*n2,maxi)
        return maxi