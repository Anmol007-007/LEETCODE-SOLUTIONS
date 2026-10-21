class Solution:
    def minReorder(self, n: int, connections: list[list[int]]) -> int:
        reach={0}
        ans=0
        while len(reach)<n:
            check=[]
            for a,b in connections:
                if b in reach:
                    reach.add(a)
                elif a in reach:
                    reach.add(b)
                    ans+=1
                else:
                    check.append([a,b])
            connections=check[::-1]
        return ans