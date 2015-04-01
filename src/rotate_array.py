# coding=utf-8
__author__ = 'cafedeflore'
class Solution:
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.
    def rotate(self, nums, k):
        size = len(nums)
        a = k % size
        if a == 0:
            return
        temp = nums[-a:] + nums[0:len(nums) - a]
        del nums[:]
        nums.extend(temp)
        return

a =Solution()
b = [1, 2, 3]
a.rotate(b, 2)
print b