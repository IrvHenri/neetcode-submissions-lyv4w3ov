class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:


        diff = {}


        for i,num in enumerate(nums):
            delta = target - num

            if delta in diff:
                return [diff[delta], i]
            
            diff[num] = i

        