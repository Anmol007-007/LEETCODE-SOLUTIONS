# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: ListNode | None) -> int:
        if not head:
            return 0
        ll=[]
        maxi=float("-inf")
        node=head
        while node:
            ll.append(node.val)
            node=node.next
        n=len(ll)
        for i in range(n//2):
            s=ll[i]+ll[n-i-1]
            maxi=max(maxi,s)
        return maxi