class Solution:
    def validPalindrome(self, s: str) -> bool:

        l,r = 0, len(s) - 1

        while l < r:

            if s[l] != s[r]:
                
                
                return self.is_palindrome_range(s, l + 1, r) or self.is_palindrome_range(s, l, r - 1)
                    
            l +=1 
            r -=1
        return True
    def is_palindrome_range(self, s,i,j):
        while i < j:
            if s[i] != s[j]:
                return False
            i+=1
            j-=1
        return True
        