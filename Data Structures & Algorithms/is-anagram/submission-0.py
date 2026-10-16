class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        seen=dict()
        seen1=dict()
        for char in t:
            if char in seen:
                seen[char]+=1
            else:
                seen[char]=1
        for char in s:
            if char in seen1:
                seen1[char]+=1
            else:
                seen1[char]=1
        if seen1==seen:
            return True
        else:
            return False
        