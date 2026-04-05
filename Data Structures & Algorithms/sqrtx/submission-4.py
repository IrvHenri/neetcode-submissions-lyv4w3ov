class Solution:
    def mySqrt(self, x: int) -> int:
        l,r = 1, x


        while l <= r:

            mid = l + ((r - l) // 2)
            
            res = mid * mid
            print(res)
            if res == x:
                return mid
            
            if res > x:
                r = mid - 1
            
            if res < x:

                l = mid + 1
        return r