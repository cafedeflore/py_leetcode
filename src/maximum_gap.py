# coding=utf-8
class Solution:
    # @param num, a list of integer
    # @return an integer
    def maximumGap(self, num):
        N = len(num)
        if N < 2:
            return 0
        total_min = min(num)
        total_max = max(num)
        buckets = {}
        ave_gap = int(1.0 * (total_max - total_min)/(N - 1))
        if ave_gap == 0:
            ave_gap = 1
        for p in num:
            index = (p - total_min) / ave_gap
            bucket = buckets.get(index)
            if bucket is None:
                bucket_temp = dict()
                bucket_temp['min'] = p
                bucket_temp['max'] = p
                buckets[index] = bucket_temp
                continue
            bucket['min'] = min(bucket['min'], p)
            bucket['max'] = max(bucket['max'], p)
        max_gap = 0
        temp_max = total_min
        if len(buckets) == 1:
            return total_max - total_min

        for i in range((total_max - total_min)/ave_gap + 1):
            if buckets.get(i) is None:
                continue
            max_gap = max(max_gap, buckets.get(i)['min'] - temp_max)
            temp_max = buckets[i]['max']

        return max_gap

a = Solution()
print a.maximumGap([3,6,9,1])