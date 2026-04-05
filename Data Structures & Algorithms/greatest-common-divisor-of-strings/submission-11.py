import math
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        if str1 + str2 != str2 + str1:
            return ''
        
        # g = math.gcd(len(str1),len(str2))
        length_1 = len(str1)
        index = float('inf')
        while length_1 > 0:
            print('s1', len(str1) % length_1)
            print('s2', len(str2) % length_1)
            if len(str1) % length_1 == 0  and len(str2) % length_1 == 0:
                index = length_1
                break
            
            length_1 -=1

        print(length_1)
        return str1[:length_1]

        
    
