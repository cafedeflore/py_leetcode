# coding=utf-8
class Solution:
    # @param num, a list of integer
    # @return an integer
    def findPeakElement(self, num):
        size = len(num)
        if size <= 0:
            return 0
        from_index = 0
        to_index = size-1
        mid_index = (from_index + to_index) / 2
        while True:
            if from_index == to_index:
                return from_index
            if from_index == mid_index:
                return from_index if num[from_index] > num[to_index] else to_index
            if num[mid_index] > num[mid_index - 1] and num[mid_index] > num[mid_index + 1]:
                return mid_index
            if num[mid_index] > num[mid_index - 1] and num[mid_index] < num[mid_index + 1]:
                from_index = mid_index + 1
                mid_index = (from_index + to_index) / 2
                continue
            else:
                to_index = mid_index - 1
                mid_index = (from_index + to_index) / 2
                continue

s = Solution()
num = [1,2,3,1]
print s.findPeakElement(num)

