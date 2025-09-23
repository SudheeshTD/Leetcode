class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        temp = set(s)

        for text in temp:
            if t.count(text) != s.count(text):
                return False
        
        return True

