class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l,r=0,k
        vowels='aeiou'
        
        count=0
        for i in range(k):
            if s[i] in vowels:
                count+=1

        max_vowel=count
        while r<len(s):
            if s[l] in vowels:
                count-=1
            if s[r] in vowels:
                count+=1
            l+=1
            r+=1
            max_vowel=max(max_vowel,count)
        return max_vowel