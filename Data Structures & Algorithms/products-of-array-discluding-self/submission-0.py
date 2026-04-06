class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        prefix = [1] * n

        for i in range(1,n):
            prefix[i] = prefix[i-1] * nums[i - 1]
        print(prefix)

        right_multiplier = 1
        for i in range (n - 1, - 1, -1):
            prefix[i] *= right_multiplier
            right_multiplier *= nums[i]

        return prefix
        