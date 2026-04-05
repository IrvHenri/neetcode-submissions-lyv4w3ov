class Solution:
    def isPalindrome(self, s: str) -> bool:

        converted_string = ''

        for char in s:
            if char.isalnum():
                converted_string += char.lower()
 
        l = 0
        r = len(converted_string) - 1

        if not converted_string or len(converted_string) < 2:
            return True


        while l < r:
            if converted_string[l] != converted_string[r]:
                return False
            l +=1
            r -=1
        
        return True
        