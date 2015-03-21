# coding=utf-8
class Solution:
    # @param version1, a string
    # @param version2, a string
    # @return an integer
    def compareVersion(self, version1, version2):
        v1 = version1.split(".")
        v2 = version2.split(".")
        for i in range(0, max(v1.__len__(), v2.__len__())):
            temp1 = 0 if not i < v1.__len__() else int(v1[i])
            temp2 = 0 if not i < v2.__len__() else int(v2[i])
            if temp1 > temp2:
                return 1
            if temp2 > temp1:
                return -1
        return 0

a = Solution()
print a.compareVersion("1.0", "1")