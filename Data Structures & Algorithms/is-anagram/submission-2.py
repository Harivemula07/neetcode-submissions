class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = {}
        countt = {}
        for ch in s:
            if ch in counts:
                counts[ch]+= 1
            else:
                counts[ch]=1
        for ch in t:
            if ch in countt:
                countt[ch]+= 1
            else:
                countt[ch]=1
        return counts==countt                        
                