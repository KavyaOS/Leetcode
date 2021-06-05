class Solution(object):
    def sortArrayByParity(self, nums):
        j, i = len(nums)-1, 0
        while i+(len(nums)-j) <= len(nums):
            if nums[i] % 2 == 0:
                if nums[j] % 2 == 0:
                    i = i + 1
                else:
                    i = i + 1
                    j = j - 1
            else:
                if nums[j] % 2 == 0:
                    temp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = temp
                    i = i + 1
                    j = j - 1
                else:
                    j = j - 1
        return nums

S = Solution()
nums = [3, 1, 2, 4]
print(S.sortArrayByParity(nums))