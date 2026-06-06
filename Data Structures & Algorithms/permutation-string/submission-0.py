class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # get length of s1 and hashmap containing letters of s1 and frequencies of each
        # sliding window approach on s2 to find if there is substring containing letters of hashmap
        # have hashmap to keep track of substring letters 
        # if two hashmaps are equal -> return true
        # if sliding window == len(s1) -> reduce window + remove letters from running hashmap if needed

        subStringLength = len(s1)
        s1Frequency = defaultdict(int)
        for char in s1:
            s1Frequency[char] += 1

        left = 0
        runningMap = defaultdict(int)
        for right in range(len(s2)):
            if s2[right] in s1Frequency:
                runningMap[s2[right]] += 1

            if runningMap == s1Frequency:
                return True

            while (right - left + 1) == subStringLength:
                if s2[left] in s1Frequency:
                    runningMap[s2[left]] -= 1
                left += 1

        return False
