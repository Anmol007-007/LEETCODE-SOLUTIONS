class Solution:
    def removeStars(self, s: str) -> str:
        n=len(s)
        ans=[]
        for i in range(n):
            if s[i]=="*":
                ans.pop()
            else:
                ans.append(s[i])
        return "".join(ans)