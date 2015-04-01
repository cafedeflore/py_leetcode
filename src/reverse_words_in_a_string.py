# coding=utf-8
__author__ = 'cafedeflore'
class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        s = s.replace("  ", " ")
        words = s.split(" ")
        res = ""
        need_blank = 0
        for i in range(len(words)):
            if words[len(words) - 1 - i] == "":
                continue
            if need_blank == 1:
                res += " "
            res += words[len(words) - 1 - i]
            need_blank = 1
        return res

a = Solution()
print a.reverseWords("")