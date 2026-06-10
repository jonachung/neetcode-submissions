class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # sliding window approach
        # t_dict = dictionary of characters of t & frequencies
        # runningDict = running dictionary to track characters.
        # charactersHave = how many characters meet required count
        # charactersNeed = how many characters need to match -> len(t_dict)
        # start, end -> -1, -1. length = math.inf

        t_dict = defaultdict(int)
        for character in t:
            t_dict[character] += 1

        runningDict = defaultdict(int)
        charactersHave = 0
        charactersNeed = len(t_dict)
        start = -1
        end = -1
        length = math.inf

        left = 0
        for right in range(len(s)):
            if s[right] in t_dict:
                runningDict[s[right]] += 1
                if runningDict[s[right]] == t_dict[s[right]]:
                    charactersHave += 1

            while charactersHave == charactersNeed:
                subStringLength = right - left + 1
                if subStringLength < length:
                    length = subStringLength
                    start = left
                    end = right

                runningDict[s[left]] -= 1
                if s[left] in t_dict and runningDict[s[left]] < t_dict[s[left]]:
                    charactersHave -= 1

                left += 1

        if length == math.inf:
            return ""
        return s[start:end+1]

                