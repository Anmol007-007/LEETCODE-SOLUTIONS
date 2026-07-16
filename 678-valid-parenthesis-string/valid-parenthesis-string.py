class Solution(object):
    def checkValidString(self, s):
        para_start=[]
        star=[]
        for i,char in enumerate(s):
            if char=="(":
                para_start.append(i)
            elif char=="*":
                star.append(i)
            else:
                if para_start:
                    para_start.pop()
                elif star:
                    star.pop()
                else:
                    return False
        while para_start and star:
            if para_start[-1]<star[-1]:
                para_start.pop()
                star.pop()
            else:
                break
        return len(para_start)==0