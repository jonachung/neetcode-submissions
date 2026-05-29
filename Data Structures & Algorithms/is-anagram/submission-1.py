class Solution:
    # hashmap for character frequency of s
    # hashmap for character frequency of t
    # loop through key of first hashmap
    # if count of character in both hashmaps are different -> return false
    # end return true
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        sFrequency = defaultdict(int)
        tFrequency = defaultdict(int)

        for c in s:
            sFrequency[c] += 1
        
        for ch in t:
            tFrequency[ch] += 1

        for key in sFrequency.keys():
            if key not in tFrequency:
                return False
            if key in tFrequency and sFrequency[key] != tFrequency[key]:
                return False

        return True