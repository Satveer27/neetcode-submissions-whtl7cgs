class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        curr = 0
        stack = []
        opHashMap = {"+":0, "-":0, "*":0, "/":0}
        for i in range(len(tokens)):
            if len(tokens) == 1:
                return int(tokens[0])

            if tokens[i] in opHashMap:
                if tokens[i] == "+":
                    curr = int(int(stack[len(stack)-1]) + int(stack[len(stack)-2]))
                if tokens[i] == "-":
                    curr = int(int(stack[len(stack)-2]) - int(stack[len(stack)-1]))
                if tokens[i] =="*":
                    curr = curr = int(int(stack[len(stack)-1]) * int(stack[len(stack)-2]))
                    print(curr)
                if tokens[i] =="/":
                    curr = curr = int(int(stack[len(stack)-2]) / int(stack[len(stack)-1]))
                    print(curr)
            
                stack.pop()
                stack.pop()
                stack.append(curr)
            else:
                stack.append(tokens[i])
            

        return curr    
