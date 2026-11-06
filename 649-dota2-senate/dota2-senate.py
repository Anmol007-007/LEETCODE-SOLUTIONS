class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r,d=deque(),deque()
        n=len(senate)
        for i in range(n):
            if senate[i]=="R":
                r.append(i)
            else:
                d.append(i)
        while r and d:
            idx1=r.popleft()
            idx2=d.popleft()
            if idx1<idx2:
                r.append(idx1+n)
            else:
                d.append(idx2+n)
        return "Radiant" if r else "Dire"