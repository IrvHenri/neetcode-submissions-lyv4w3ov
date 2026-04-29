class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        token_list = {'+','-','/','*'}
        for token in tokens:
            if token not in token_list:
                stack.append(int(token))
            elif token == '+':
                operand_two = stack.pop()
                operand_one = stack.pop()
                sum_total = operand_one + operand_two
                stack.append(sum_total)
            
            elif token == '-':
                operand_two = stack.pop()
                operand_one = stack.pop()
                delta = operand_one - operand_two
                stack.append(delta)
            
            elif token == '*':
                operand_two = stack.pop()
                operand_one = stack.pop()
                product = operand_one * operand_two
                stack.append(product)
            elif token == '/':

                operand_two = stack.pop()
                operand_one = stack.pop()
                remainder = int(operand_one / operand_two)
                stack.append(remainder)


        return stack[-1]
        