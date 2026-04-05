class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        stack = [trust[0][1]]

        for i in range(1,len(trust)):
            trusted = trust[i][1]
            if trusted != stack[-1]:
                return -1
        
        return stack[-1]



        



        