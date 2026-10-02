class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        res=[]
        def back(start,st,n,k):
            if n==0 and k==0:
                res.append(st[:])
                return
            for i in range(start,10):
                if i>n or k<=0:
                    break
                st.append(i)
                back(i+1,st,n-i,k-1)
                st.pop()
        back(1,[],n,k)
        return res