class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel=[i for i in s if i in "aeiouAEIOU"]
        result=[i if i not in "aeiouAEIOU" else vowel.pop() for i in s ]
        return "".join(result)