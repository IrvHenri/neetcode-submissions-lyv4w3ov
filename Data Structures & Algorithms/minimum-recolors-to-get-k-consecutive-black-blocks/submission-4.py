class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:

        count = 0
        l = 0
        ans = k
        

        for r in range(len(blocks)):
            block = blocks[r]

            if block == 'W':
                count +=1
            if r - l + 1 == k:
                ans = min(ans, count)
                if blocks[l] == 'W':
                    count -= 1 
                l +=1

        return ans