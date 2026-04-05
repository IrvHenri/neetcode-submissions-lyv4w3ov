import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.stones = stones
        heapq.heapify_max(self.stones)
        
        while len(self.stones) > 1:
            x = heapq.heappop_max(self.stones)
            y = heapq.heappop_max(self.stones)

            if x == y:
                continue
            
            if x < y:
                y = y - x
                heapq.heappush_max(self.stones,y)
            else:
                x = x - y
                heapq.heappush_max(self.stones,x)
        if self.stones:
            return self.stones[0]
        return 0


        