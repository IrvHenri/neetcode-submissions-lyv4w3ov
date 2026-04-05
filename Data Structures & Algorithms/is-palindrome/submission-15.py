class Solution:
    def isPalindrome(self, s: str) -> bool:
       

        alnum_string = []

        for char in s:
            if char.isalnum():
                alnum_string.append(char.lower())

        alnum_string = ''.join(alnum_string)
        l = 0
        r = len(alnum_string) - 1
        
        while l < r:

            if alnum_string[l] != alnum_string[r]:
                return False 

            l +=1
            r -=1

        return True

        