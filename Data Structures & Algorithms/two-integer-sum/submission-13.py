class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        sumMap = {}
        result = None
        for i,num in enumerate(nums):

            delta = target - num

            if delta in sumMap:
                result = [i,sumMap[delta]]
            else:
                sumMap[num] = i
 
        return sorted(result)