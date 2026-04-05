class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        k = 0
        l = 0

        for r in range(len(nums)):
            if nums[r] != val:
                nums[r],nums[l] = 0, nums[r]
                k +=1
                l +=1


        return k
        