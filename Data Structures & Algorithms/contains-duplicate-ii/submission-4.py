class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen_map = {}

        for i, num in enumerate(nums):

            if num in seen_map:
                if abs(i - seen_map[num]) <= k:
                    return True
                else:
                    seen_map[num] = i
                

            seen_map[num] = seen_map.get(num,i)

            
        
        return False
        