class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 1
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                # unique value found and store at j
                nums[j] = nums[i]
                # move up unique spot by 1
                j +=1
        return j

        