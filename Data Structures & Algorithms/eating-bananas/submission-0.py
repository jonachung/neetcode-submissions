class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        answer = math.inf
        left = 1
        right = max(piles)

        while left <= right:

            mid = (left + right) // 2

            total = 0
            for pile in piles:
                total += math.ceil(pile / mid)
            if total > h:
                left = mid + 1
            else:
                answer = min(answer, mid)
                right = mid - 1

        return answer