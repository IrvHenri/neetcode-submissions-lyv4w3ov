class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        trust_record = [trust[0][1]]
        judge_exists = True
        for i in range(1,len(trust)):
            trusted = trust[i][1]
           
            if trusted not in trust_record:
                judge_exists = False
                break
        
        if not judge_exists:
            return -1
        return trust_record[0]



        