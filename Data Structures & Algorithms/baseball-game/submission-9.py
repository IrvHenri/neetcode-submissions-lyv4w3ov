class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        sum_scores = 0
        for op in operations:
            try:
                record.append(int(op))
            except:
    
                if op == '+':
                    last_score = record[-1]
                    second_last_score = record[-2]
                    sum_score = last_score + second_last_score
                    record.append(sum_score) 
                if op == 'D':
                    double_score = record[-1] * 2
                    record.append(double_score)
                if op == 'C':
                    record.pop()
        
        
        print(record)
        return sum(record)   
        