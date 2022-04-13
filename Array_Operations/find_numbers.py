class Solution(object):
    def findNumbers(self, nums):
        num_evens = num_digits = 0
        for num in nums:
            while num != 0:
                num_digits += 1
                num = num//10
            if num_digits%2 == 0:
                num_evens = num_evens + 1
            num_digits = 0

        return num_evens

print(Solution().findNumbers([555,901,482,1771]))