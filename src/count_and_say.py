__author__ = 'Nan'

class Solution:
    # @return a string

    def countAndSay(self, n):
        if n == 1:
            return "1"
        res = "1"
        for i in range(0, n - 1):
            res = self.count(res)
        return res
        # self.count(str(n))

    def count(self, seq):
        if len(seq) < 1:
            print "no"
            return
        p2 = 0
        p_max = len(seq) - 1
        type = seq[p2]
        count = 0
        result = ""
        while True:
            if seq[p2] == type:
                count += 1
                p2 += 1
            else:
                result += "%d%s" % (count, type)
                type = seq[p2]
                count = 0
            if p2 > p_max:
                result += "%d%s" % (count, type)
                break
        print result
        return result

s = Solution()
s.countAndSay(5)