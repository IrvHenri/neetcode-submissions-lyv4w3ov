class Solution:
    def isHappy(self, n: int) -> bool:

        str_int = str(n)
        seen = set()
        
        while str_int:
            sum_of_squares = 0
            
            for char in str_int:
               sum_of_squares += (int(char) * int(char))
            
            if sum_of_squares == 1:
                    return True
            elif sum_of_squares in seen:
                return False
            
            seen.add(sum_of_squares)
            str_int = str(sum_of_squares)
            sum_of_squares = 0



        return True





        