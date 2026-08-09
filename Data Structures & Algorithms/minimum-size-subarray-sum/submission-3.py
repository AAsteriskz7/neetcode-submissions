class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = float('inf')
        total = 0
        L = 0

        for R in range(len(nums)):
            total += nums[R]

            while total >= target:
                min_len = min(min_len, R - L + 1)
                total -= nums[L]
                L += 1

        return min_len if min_len != float('inf') else 0