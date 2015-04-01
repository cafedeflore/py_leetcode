# coding=utf-8
__author__ = 'cafedeflore'
class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        num = 0
        for i in range(32):
            if n % 2 == 1:
                num += 1
            n /= 2
        return num

S = Solution()
print S.hammingWeight(11)