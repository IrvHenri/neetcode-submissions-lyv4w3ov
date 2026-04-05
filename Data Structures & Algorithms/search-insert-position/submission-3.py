class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums) - 1

        while l <= r:

            mid = l + ((r-l) // 2)
            mid_val = nums[mid]

            if mid_val == target:
                return mid
            
            if mid_val > target:
                r = mid - 1

            if mid_val < target:
                l = mid + 1
            
        return l


            
        