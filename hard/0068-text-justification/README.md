# Text Justification

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

Given an array of strings `words` and a width `maxWidth`, format the text such that each line has exactly `maxWidth` characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces `' '` when necessary so that each line has exactly `maxWidth` characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified, and no extra space is inserted between words.

**Note:**

- A word is defined as a character sequence consisting of non-space characters only.
- Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
- The input array words contains at least one word.

 

**Example 1:**

```
Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
```

**Example 2:**

```
Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.
Note that the second line is also left-justified because it contains only one word.
```

**Example 3:**

```
Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
```

 

**Constraints:**

- 1 <= words.length <= 300
- 1 <= words[i].length <= 20
- words[i] consists of only English letters and symbols.
- 1 <= maxWidth <= 100
- words[i].length <= maxWidth

## Solution

**Language:** Python  
**Runtime:** 0 ms (beats 100.00%)  
**Memory:** 19.3 MB (beats 68.21%)  
**Submitted:** 2026-11-20T05:09:40.400Z  

```py
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
```

---

[View on LeetCode](https://leetcode.com/problems/text-justification/)