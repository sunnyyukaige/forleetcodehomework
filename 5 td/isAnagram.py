class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s)!=len(t):
            return False
        return sorted(s)==sorted(t)

    def isAnagramP1(self, s: str, t: str) -> bool:
        
        if len(s)!=len(t):
            return False
        for i in s:
            if t.count(i)!=s.count(i):
                return False
            else:
                 return True