class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Track duplicates
        window = set()
        # Track left most of the window
        L = 0

        for R in range(len(nums)):

            if R - L > k:
                window.remove(nums[L])
                L +=1
            if nums[R] in window:
                return True
            window.add(nums[R])
        return False
