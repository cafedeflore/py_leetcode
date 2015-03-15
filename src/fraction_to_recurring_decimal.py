# coding=utf-8
class Solution:
    # @return a string
    def fractionToDecimal(self, numerator, denominator):
        res = ""
        if denominator == 0:
            raise Exception
        if numerator / denominator < 0:
            res = "-"
        numerator = abs(numerator)
        denominator = abs(denominator)
        integer_part = self.get_integer_part(numerator, denominator)
        fractional_part = self.get_fractional_part(numerator, denominator)
        if fractional_part is not None and fractional_part != "":
            res += integer_part + "." + fractional_part
        else:
            res += integer_part
        # print res
        return res

    def get_integer_part(self, numerator, denominator):
        if denominator == 0:
            raise Exception
        return str(numerator/denominator)

    def get_fractional_part(self, numerator, denominator):
        res = ""
        deno_set = []
        nu = numerator
        de = denominator
        if denominator == 0:
            raise Exception
        if(nu >= de):
            nu %= de
        nu *= 10
        while nu not in deno_set and nu != 0:
            deno_set.append(nu)
            res += str(nu / de)
            nu %= de
            nu *= 10
        if nu == 0:
            return res
        else:
            index = deno_set.index(nu)
            res = res[0:index] + "(" + res[index:] + ")"
        return res

a = Solution()
a.fractionToDecimal(2, 1)