class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        res,i,n=[],0,len(words)

        while i<n:
            j=i
            line_l=0
            while j<n and line_l+len(words[j])+(j-i)<=maxWidth:
                line_l += len(words[j])
                j+=1
            space_count=maxWidth-line_l
            gaps=j-i-1
            line=""
            if j==n or gaps==0:
                for i in range(i,j):
                    line+=words[i]+(" " if i!=j-1 else "")
                line +=" "*(maxWidth-len(line))
            else:
                spaces=space_count//gaps
                extra=space_count% gaps
                for i in range(i,j):
                    line += words[i]
                    if i!=j-1:
                        ad=spaces+(1 if extra>0 else 0)
                        line +=" "*ad
                        if extra>0:
                            extra-=1
            res.append(line)
            i=j
        return res