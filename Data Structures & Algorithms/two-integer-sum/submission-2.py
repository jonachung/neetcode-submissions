class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hashmap to add number,index
        # loop through index of nums
        # if target - nums[index] in hashmap
        # return [index, map[target - nums[index]]]

        map = defaultdict(int)
        for i in range(len(nums)):
            if (target - nums[i]) in map:
                return [map[target - nums[i]], i]
            map[nums[i]] = i

        return []