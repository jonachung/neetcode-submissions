class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        frequencyMap = defaultdict(int)
        for num in nums:
            frequencyMap[num] += 1

        for key, value in frequencyMap.items():
            if value == 1:
                return key

        return -100000