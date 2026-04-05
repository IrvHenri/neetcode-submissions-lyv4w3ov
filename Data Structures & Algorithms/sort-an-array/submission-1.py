class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        if len(nums) <= 1:
            return nums
        
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]

        sorted_right = self.sortArray(right)
        sorted_left = self.sortArray(left)

        return self.merge(sorted_left,sorted_right)

    def merge(self,left,right):
        res = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                res.append(left[i])
                i +=1
            else:
                res.append(right[j])
                j +=1
        
        res.extend(left[i:])
        res.extend(right[j:])

        return res
        