class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        count = [0] * 26


        for i in range(len(s)):
            ord_s = ord(s[i]) - ord('a')
            ord_t = ord(t[i]) - ord('a')

            count[ord_s] +=1
            count[ord_t] -=1
        
        for val in count:
            if val != 0:
                return False
        
        return True
        