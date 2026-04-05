class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        k = 0

        left = 0

        for i , num in enumerate(nums):
            if num != val:
                nums[left] = num
    
                left +=1
                k +=1
        print(nums)
        return k
        