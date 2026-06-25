class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # get frequencyMap of t
        # sliding window algorithm to find substring that has letters + same count as t
        # subStringLength = math.inf
        # start, end = -1, -1
        # runningDict to hold characters in current window (just hold if letters are same as t)
        # charactersHave
        # charactersNeed

        subStringLength = math.inf
        start = -1
        end = -1

        tFrequency = defaultdict(int)
        for character in t:
            tFrequency[character] += 1

        charactersNeed = len(tFrequency)

        left = 0
        running = defaultdict(int)
        for right in range(len(s)):
            if s[right] in tFrequency:
                running[s[right]] += 1
                if running[s[right]] == tFrequency[s[right]]:
                    charactersNeed -= 1

            while charactersNeed == 0:
                length = right - left + 1
                if length < subStringLength:
                    start = left
                    end = right
                    subStringLength = length

                if s[left] in tFrequency:
                    running[s[left]] -= 1
                    if running[s[left]] < tFrequency[s[left]]:
                        charactersNeed += 1

                left += 1

        if subStringLength == math.inf:
            return ""
        return s[start:end+1]


        