class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        
        res = ''

        for i in range(len(strs[0])):
            char_to_match = strs[0][i]
            for s in strs:
                # Check if index is out of bounds or character mismatch
                if i == len(s) or s[i] != char_to_match:
                    return res
            res += char_to_match



        return res
            
                
            
                

            


            


        