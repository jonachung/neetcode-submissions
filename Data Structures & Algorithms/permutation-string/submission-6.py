class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # get subStringLength of s1
        # get frequencyMap of s1
        # sliding window to find substring that is permutation of s1
        # keep global running frequency map
        # if s2[right] in frequencyMap: runningMap[s2[right]] += 1
        # if runningMap == frequencyMap: return True
        # while (right - left + 1) > subStringLength:
        #    if s2[left] in frequencyMap -> runningMap[s2[right]] -= 1
        #.   left += 1
        #.return false

        # O(min(len(s1), len(s2))) time
        # O(len(s1) + len(s2)) space (frequency dictionaries mainly)


        subStringLength = len(s1)
        s1FrequencyMap = defaultdict(int)

        for character in s1:
            s1FrequencyMap[character] += 1

        left = 0
        runningMap = defaultdict(int)
        for right in range(len(s2)):
            if s2[right] in s1FrequencyMap:
                runningMap[s2[right]] += 1

            if runningMap == s1FrequencyMap:
                return True

            while (right - left + 1) == subStringLength:
                if s2[left] in s1FrequencyMap:
                    runningMap[s2[left]] -= 1
                left += 1

        return False
