__author__ = 'Nan'
class Solution:
    # @return a boolean
    def isValid(self, s):
        if len(s) % 2 != 0 or len(s) == 0:
            return False
        kuohao = {']': '[', '}': '{', ')': '('}
        left = set()
        for (x, y) in kuohao.items():
            left.add(y)

        stack = ""
        if (s[0]) not in left:
            return False
        for i in range(len(s)):
            if s[i] in left:
                stack += s[i]
            elif s[i] in kuohao:
                if len(stack) < 1 or stack[-1] != kuohao[s[i]]:
                    return False
                else:
                    stack = stack[0:-1]
        if len(stack) != 0:
            return False
        return True


s = Solution()
print s.isValid("((")