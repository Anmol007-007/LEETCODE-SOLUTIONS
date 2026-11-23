# Substring with Concatenation of All Words

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

You are given a string `s` and an array of strings `words`. All the strings of `words` are of **the same length**.

A **concatenated string** is a string that exactly contains all the strings of any permutation of `words` concatenated.

- For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not a concatenated string because it is not the concatenation of any permutation of words.

Return an array of *the starting indices* of all the concatenated substrings in `s`. You can return the answer in **any order**.

 

Original
Python3
**Example 1:**

**Input:** s = "barfoothefoobarman", words = ["foo","bar"]

**Output:** [0,9]

**Explanation:**

The substring starting at 0 is `"barfoo"`. It is the concatenation of `["bar","foo"]` which is a permutation of `words`.
The substring starting at 9 is `"foobar"`. It is the concatenation of `["foo","bar"]` which is a permutation of `words`.

**Example 2:**

**Input:** s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]

**Output:** []

**Explanation:**

There is no concatenated substring.

**Example 3:**

**Input:** s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]

**Output:** [6,9,12]

**Explanation:**

The substring starting at 6 is `"foobarthe"`. It is the concatenation of `["foo","bar","the"]`.
The substring starting at 9 is `"barthefoo"`. It is the concatenation of `["bar","the","foo"]`.
The substring starting at 12 is `"thefoobar"`. It is the concatenation of `["the","foo","bar"]`.

 

**Constraints:**

- 1 <= s.length <= 104
- 1 <= words.length <= 5000
- 1 <= words[i].length <= 30
- s and words[i] consist of lowercase English letters.

## Solution

**Language:** Python  
**Runtime:** 21 ms (beats 84.10%)  
**Memory:** 19.7 MB (beats 75.18%)  
**Submitted:** 2026-11-23T06:07:02.638Z  

```py
from typing import List
from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        res = []
        n, k = len(s), len(words[0])
        total = len(words)
        expected = Counter(words)

        for offset in range(k):
            left = offset
            seen = Counter()
            count = 0

            for right in range(offset, n - k + 1, k):
                word = s[right:right + k]

                if word not in expected:
                    seen.clear()
                    count = 0
                    left = right + k
                    continue

                seen[word] += 1
                count += 1

                while seen[word] > expected[word]:
                    seen[s[left:left + k]] -= 1
                    left += k
                    count -= 1

                if count == total:
                    res.append(left)

        return res
```

---

[View on LeetCode](https://leetcode.com/problems/substring-with-concatenation-of-all-words/)