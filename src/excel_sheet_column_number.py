__author__ = 'Nan'
class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
        if not s.isalpha():
            raise Exception
        s = s.lower()
        res = 0
        for i in range(len(s)):
            res = res * 26 + ord(s[i]) - ord('a') + 1
        # print res
        return res

s = Solution()
s.titleToNumber("aa")