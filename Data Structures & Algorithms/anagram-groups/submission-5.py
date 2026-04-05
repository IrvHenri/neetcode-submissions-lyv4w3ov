class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # ord(char) - ord(a) > add to total as key,
        tracker = {}

        for str in strs:
            sorted_str = ''.join(sorted(str))
            
            if sorted_str in tracker:
                tracker[sorted_str].append(str)

            else:
                tracker[sorted_str] = [str]
        
        return list(tracker.values())
        