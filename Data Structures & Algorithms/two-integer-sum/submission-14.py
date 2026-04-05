class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        sumMap = {}
        result = None
        for i,num in enumerate(nums):

            delta = target - num

            if delta in sumMap:
                result = [sumMap[delta],i]
            else:
                sumMap[num] = i
 
        return result