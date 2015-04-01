# coding=utf-8
__author__ = 'cafedeflore'
class Solution:

    def jia(x, y):
        return x + y

    def jian(x, y):
        return x - y

    def cheng(x, y):
        return x * y

    def chu(x, y):
        if x * y < 0:
            return -((-x) / y)
        return x / y

    cal = {
        "+": jia,
        "-": jian,
        "*": cheng,
        "/": chu
    }
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        # if tokens == ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]:
        #     return 22
        list = ["+", "-", "*", "/"]
        nums = []
        for i in range(len(tokens)):
            if tokens[i] not in list:
                nums.append(tokens[i])
                continue
            # print nums
            b = int(nums.pop())
            a = int(nums.pop())
            nums.append(self.cal.get(tokens[i])(a, b))
            # print nums
        return int(nums.pop())

a = Solution()
print a.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])