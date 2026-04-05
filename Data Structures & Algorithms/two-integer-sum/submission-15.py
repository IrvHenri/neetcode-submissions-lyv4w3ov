class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        remainder_map = {}

        for i, num in enumerate(nums):
            remainder = target - num

            if remainder in remainder_map:

                return [remainder_map.get(remainder),i]
            
            remainder_map[num] = i

        