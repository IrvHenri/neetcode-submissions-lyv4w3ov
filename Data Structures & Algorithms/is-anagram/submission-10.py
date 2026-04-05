class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        frequency_map = {}

        for char in s:
            frequency_map[char] = frequency_map.get(char,0) + 1
        
        for char in t:
            if char not in frequency_map:
                return False
            
            frequency_map[char] = frequency_map.get(char) - 1

        return all(x == 0 for x in frequency_map.values())