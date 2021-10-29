'''https://leetcode.com/problems/reverse-integer/'''

class Solution(object):
    def reverse(self, x):
        str_value = str(x)
        result = ""
        if str_value[0] == '-':
            result = str_value[-1:0:-1]
            result = '-' + result
        else:
            result = str_value[::-1]
        if int(result)>=2**31 or int(result)<-2**31:
            return 0
        return int(result)

print(Solution().reverse(-67567))