__author__ = 'Nan'
class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        if len(s) <= 1:
            return len(s)

        p1 = 0
        p2 = 0
        max_p = len(s)

        c_set = set()
        count = 0
        max_count = 1
        while p2 < max_p:
            if s[p2] not in c_set:
                c_set.add(s[p2])
                count += 1
                p2 += 1
                continue
            max_count = count if count >= max_count else max_count
            while p1 < p2:
                if s[p1] == s[p2]:
                    count = p2 - p1
                    p1 += 1
                    p2 += 1
                    break
                c_set.remove(s[p1])
                p1 += 1
        max_count = count if count >= max_count else max_count
        return max_count

s = Solution()
print s.lengthOfLongestSubstring("12331")