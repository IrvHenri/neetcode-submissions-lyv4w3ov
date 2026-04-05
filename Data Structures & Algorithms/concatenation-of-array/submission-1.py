class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        ans = list(nums)

        for i, num in enumerate(nums):
            ans.append(nums[i])
            
        return ans
        