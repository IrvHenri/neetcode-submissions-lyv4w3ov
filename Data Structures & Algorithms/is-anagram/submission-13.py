class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        ord_map = {}

        for i in range(len(s)):
            

            if s[i] not in ord_map:
                ord_map[s[i]] = 1
            else:

                ord_map[s[i]] = ord_map[s[i]] + 1

        for i in range(len(t)):


            if t[i] not in ord_map:
                 ord_map[t[i]] = 1
            else:
                 ord_map[t[i]] = ord_map[t[i]] - 1    


 
        for val in ord_map.values():
            if val != 0:
                return False
        return True
        