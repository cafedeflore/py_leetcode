# coding=utf-8
class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        size = len(num)
        from_index = 0
        to_index = size - 1
        mid_index = (from_index + to_index) / 2
        while from_index != to_index:
            # head = num[from_index]
            end = num[to_index]
            mid = num[mid_index]
            if mid > end:
                from_index = mid_index + 1
                mid_index = (from_index + to_index) / 2
            elif mid == end:
                return min(self.findMin(num[from_index:mid_index + 1]), self.findMin(num[mid_index:-1]))
            else:
                to_index = mid_index
                mid_index = (from_index + to_index) / 2
        return num[from_index]

a = Solution()
p = [3,1,3,3,3,3]
# print p[0:1]
print a.findMin(p)