class Solution:
    def tribonacci(self, n: int) -> int:
        tribonacci_number = [0,1,1]
        if n < 1:
            return 0
        if n < 2:
             return 1   
        for i in range(3,n + 1):

            val = tribonacci_number[-1] + tribonacci_number[-2] + tribonacci_number[-3]
            tribonacci_number.append(val)

        return tribonacci_number[-1]
        