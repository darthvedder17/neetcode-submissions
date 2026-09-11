class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        evals = {"+","-","/","*"}
        res = 0
        for token in tokens:
            if token not in evals:
                stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()
                if token == "+":
                    res = a + b
                elif token == "-":
                    res = a - b
                elif token == "*":
                    res = a * b
                else:
                    res = int(a/b)
                stack.append(res)
        return stack[0]                
        