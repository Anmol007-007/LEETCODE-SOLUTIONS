class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        ans=[0]*len(temperatures)
        st=[]
        for i,temp in enumerate(temperatures):
            while st and temp>temperatures[st[-1]]:
                idx=st.pop()
                ans[idx]=i-idx
            st.append(i)
        return ans