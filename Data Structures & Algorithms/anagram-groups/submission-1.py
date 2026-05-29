class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = []
        map = defaultdict(list)
        for str in strs:
            sortedString = "".join(sorted(str))
            map[sortedString].append(str)

        for key, value in map.items():
            answer.append(value)

        return answer