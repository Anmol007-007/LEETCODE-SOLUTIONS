class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        count=Counter(arr)
        occ=count.values()
        s=set(occ)
        if len(s)==len(occ):
            return True
        return False

