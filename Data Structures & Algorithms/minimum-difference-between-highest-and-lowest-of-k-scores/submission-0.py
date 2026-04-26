class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        l = 0
        sorted_nums = sorted(nums)
        min_delta = float('inf')

        for r in range(len(sorted_nums)):
            if r - l + 1 == k:
                min_delta = min(min_delta,sorted_nums[r] - sorted_nums[l])
                l +=1
        return min_delta
        