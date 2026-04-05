class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # two pointers, while left is less then length or right is less then length
            # increment left and right

            l,r = 0,0
            res = ''
            while l < len(word1) or r < len(word2):

                if l < len(word1):
                    res += word1[l] 
                
                if r < len(word2):
                    res += word2[r]  
                l +=1
                r +=1
            
            return res

        