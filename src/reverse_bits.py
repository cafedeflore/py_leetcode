# coding=utf-8
__author__ = 'cafedeflore'
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        res = 0
        for i in range(32):
            res = (res << 1)
            res += n % 2
            n /= 2
        return res

S = Solution()
print S.reverseBits(43261596)