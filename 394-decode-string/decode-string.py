class Solution:
    def decodeString(self, s: str) -> str:
        ans=[]
        for i in s:
            if i!="]":
                ans.append(i)
            else:
                curr_str=""
                while ans[-1]!="[":
                    curr_str=ans.pop()+curr_str
                ans.pop()
                curr_num=""
                while ans and ans[-1].isdigit():
                    curr_num=ans.pop()+curr_num
                curr_str=int(curr_num)*curr_str
                ans.append(curr_str)
        return "".join(ans)