class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        tracker = {}

        for num in nums:
            if num not in tracker:
                tracker[num] = 1
            else:
                tracker[num] +=1
        print(tracker)
        sorted_dict = dict(sorted(tracker.items(), key=lambda item: item[1]))
        print(sorted_dict)
        return list(sorted_dict)[-k:]
        