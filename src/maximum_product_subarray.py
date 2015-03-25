# coding=utf-8
class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxProduct(self, A):
        if len(A) < 1:
            return 0
        max_product = A[0]
        from_index = 0
        zero_count = 0
        for i in range(len(A)):
            if A[i] == 0:
                zero_count += 1
                max_product = max(max_product, self.get_max_product(A[from_index:i])) if len(A[from_index:i]) > 0 else max_product
                from_index = i+ 1
        max_product = max(max_product, self.get_max_product(A[from_index:])) if len(A[from_index:]) > 0 else max_product
        if max_product < 0 and zero_count > 0:
            return 0
        return max_product

    def get_max_product(self, A):
        if len(A) == 1:
            return A[0]
        nega_count = 0
        product = 1
        first_index = -1
        last_index = -1
        for i in range(len(A)):
            product *= A[i]
            if A[i] < 0:
                if first_index == -1:
                    first_index = i
                last_index = i
                nega_count += 1
        if nega_count % 2 == 0:
            return product
        else:
            first_product = 1
            last_product = 1
            for i in A[0:first_index + 1]:
                first_product *= i
            for i in A[last_index:]:
                last_product *= i
            # print product
            # print first_product
            # print last_product
            return product / first_product if first_product > last_product else product / last_product

p = [-1]
a = Solution()
print a.get_max_product(p)
print a.maxProduct(p)