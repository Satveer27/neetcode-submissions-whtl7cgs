class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        curr_exp = ""
        stack = []
        hashMap = {"+":0, "-":1, "/":2, "*":3}
        
        for i in tokens:
            if i not in hashMap:
                stack.append(int(i))
            else:
                second_num = stack.pop()
                first_num = stack.pop()
                if i == "+":
                    stack.append(first_num + second_num)
                elif i == "*":
                    stack.append(first_num * second_num)
                elif i == "-":
                    stack.append(first_num - second_num)
                elif i =="/":
                    stack.append(int(first_num / second_num))
        
        return stack.pop()

            

    

